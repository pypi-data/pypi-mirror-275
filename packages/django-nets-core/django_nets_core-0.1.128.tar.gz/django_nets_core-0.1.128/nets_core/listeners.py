from nets_core.firebase_messages import send_user_device_notification
from nets_core.models import NetsCoreBaseModel, VerificationCode
from django.db.models.signals import post_delete, post_save, pre_delete, post_migrate, post_init, pre_save
from django.dispatch import receiver
from nets_core.mail import send_email
from nets_core.models import EmailTemplate
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

import logging

logger = logging.getLogger(__name__)


@receiver(pre_save)
def pre_save_base_model_handler(sender, instance, **kwargs):
    if not instance.pk:
        return # created
    
    if issubclass(sender, NetsCoreBaseModel):
        # NetsCoreBaseModel implements updated_fields property to track fields that have changed
        # is a dict of field_name: [{'old': old_value, 'new': new_value, 'time': time}]
        untracked_fields = ['password', 'token', 'updated_fields']
        previous_instance = sender.objects.get(pk=instance.pk)
        for field in instance._meta.fields:
            if not hasattr(field, 'column') or field.column in ('created_at', 'updated_at'):
                continue
            # check if field is auto_now or auto_now_add
            if field.auto_now or field.auto_now_add:
                continue
            
            field_name = field.name
            if field_name in untracked_fields:
                continue
            
            if getattr(previous_instance, field_name) != getattr(instance, field_name):
                if not hasattr(instance, 'updated_fields'):
                    instance.updated_fields = {}
                if field_name not in instance.updated_fields:
                    instance.updated_fields[field_name] = []
                
                # ensure values are strings for JSON serialization
                try:
                    old_value = str(getattr(previous_instance, field_name))
                except:
                    old_value = None
                
                try:
                    new_value = str(getattr(instance, field_name))
                except:
                    new_value = None
                
                if not old_value and not new_value:
                    continue
                
                if old_value != new_value:
                    instance.updated_fields[field_name].append({
                        'old': old_value,
                        'new': new_value,
                        'time': str(timezone.now())
                    })


@receiver(post_save, sender=VerificationCode)
def send_verification_code_email(sender, instance, created, **kwargs):
    if created:
        # send email
        cache_token_key = instance.get_token_cache_key()
        button_link = {"url": "", "label": cache.get(cache_token_key)}
        template = None
        html = None
        email_template = (
            EmailTemplate.objects.filter(use_for="verification_code", enabled=True)
            .order_by("-created")
            .first()
        )

        if email_template:
            html = email_template.html_body
        else:
            template = "nets_core/email/verification_code.html"

        result = send_email(
            _("Verification code"),
            [instance.user.email],
            template,
            {"button_link": button_link, "user": instance.user},
            html=html,
            to_queued=False,
        )
        logger.info(
            f"Verification code email to {instance.user.email} with result {result}"
        )

    else:
        if instance.verified:
            # send notification to user about new login
            template = "nets_core/email/new_login.html"
            send_email(
                _("New login"),
                [instance.user.email],
                template,
                {"user": instance.user, "ip": str(instance.ip), "device": instance.device},
                to_queued=False,
            )

            message = _("New login to your account from ip address") + " " + instance.ip
            data = {"type": "login", "ip": str(instance.ip), "device": ""}
            if instance.device:
                message += " " + _("using device") + " " + instance.device.__str__()
                data["device"] = f"{instance.device.name}"
                data["device_id"] = f"{instance.device_id}"
            title = f"{_('New login')} {instance.user.username}"
            send_user_device_notification(
                instance.user, title=title, message=message, data=data
            )
