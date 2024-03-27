from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def set_is_teacher_false(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        instance.is_teacher = False
        instance.save()