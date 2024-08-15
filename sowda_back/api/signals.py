from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=UserProd)
def user_created(sender, instance, created, **kwargs):
    if created:
        # Perform any actions you want to take when a new product is created
        print(f"Täze ulanyjy: {instance.author}")