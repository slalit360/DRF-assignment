import logging

from django.core.mail import send_mail
from assignment.settings import EMAIL_HOST_USER

logger = logging.getLogger(__name__)


def send_notification(user_email, subject, message):
    try:
        sent = send_mail(subject, message, EMAIL_HOST_USER, [user_email], fail_silently=False)
        logger.info("Email sent on query answered :", sent)
    except Exception as e:
        logger.error("failed to send email : ", e)
