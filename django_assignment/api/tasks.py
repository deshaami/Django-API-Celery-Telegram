from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_welcome_email(to_email):
    subject = 'Welcome to My App'
    message = 'Thanks for registering!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [to_email]

    try:
        sent_count = send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,  # So errors will raise exceptions
        )
        logger.info(f"Email sent to {to_email}, count: {sent_count}")
        return f"Email sent to {to_email}"
    except Exception as e:
        logger.error(f"Error sending email to {to_email}: {e}")
        raise e
