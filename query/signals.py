from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AnswerQuery
from .util import send_notification


@receiver(post_save, sender=AnswerQuery)
def notify_user(sender, instance, created, **kwargs):
    # print(sender)
    # print(instance)
    if created:
        target_user_email = instance.query.user.email
        target_user_name = instance.query.user.name
        answered_by = instance.answered_by
        subject = "Your Query is answered!"
        message = "Hi {}, \n your query is answered by {}".format(target_user_name, answered_by)
        send_notification(target_user_email, subject, message)
        # print(subject, message)
