from django.core.mail import send_mail

from assignment.settings import EMAIL_HOST_USER


def send_notification(user_email, subject, message):
    sent = send_mail(subject, message, EMAIL_HOST_USER, [user_email], fail_silently=False)
    print(sent)
