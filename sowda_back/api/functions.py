from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
import bcrypt

@receiver(post_save, sender=UserProd)
def user_created(sender, instance, created, **kwargs):
    if created:
        # Perform any actions you want to take when a new product is created
        print(f"Täze ulanyjy: {instance.username}")

def hash_password(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    return hashed_password

def verify_password(plain_password, hashed_password):
    # Convert the plain password to bytes
    plain_password_bytes = plain_password.encode('utf-8')
    
    # Check if the hashed password matches the plain password
    return bcrypt.checkpw(plain_password_bytes, hashed_password)
