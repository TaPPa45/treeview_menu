from datetime import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import MenuItem


@receiver(pre_save, sender=MenuItem)
def normalize_menuitem_url(sender, instance, **kwargs):
    if not instance.url.endswith("/"):
        instance.url += "/"
    if not instance.url.startswith("/"):
        instance.url = "/" + instance.url
