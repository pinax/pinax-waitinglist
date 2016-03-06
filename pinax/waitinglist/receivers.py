from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Survey, SurveyInstance, WaitingListEntry


@receiver(post_save, sender=WaitingListEntry)
def handle_waitinglistentry_save(sender, **kwargs):
    if kwargs.get("created"):
        try:
            survey = Survey.objects.get(active=True)
            SurveyInstance.objects.create(
                survey=survey,
                entry=kwargs.get("instance")
            )
        except Survey.DoesNotExist:
            pass
