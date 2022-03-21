from django.dispatch import receiver
from django.db.models.signals import post_delete,post_save
from .models import UserAccount
from django.contrib.auth.models import User


@receiver(post_save, sender = User)
def create_account(sender, created, instance, **kwargs):
    if created:
        user = instance
        user_account = UserAccount.objects.create(
            owner = user,
            first_name = user.first_name,
            last_name = user.last_name,
            username = user.username,
            email = user.email,
        )

@receiver(post_delete, sender = UserAccount)
def delete_user_account(sender,instance,**kwargs):
    instance.delete