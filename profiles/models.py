from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from djstripe.models import Customer, Subscription


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    stripeCustomerId = models.CharField(max_length=255, null=True, blank=True)
    stripeCustomer = models.ForeignKey(
        Customer, null=True, blank=True, on_delete=models.SET_NULL
    )
    stripeSubscriptionId = models.CharField(max_length=255, null=True,
                                            blank=True)
    stripeSubscription = models.ForeignKey(
        Subscription, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # For existing users, save the profile
    instance.userprofile.save()
