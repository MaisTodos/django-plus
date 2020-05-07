import logging

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)


DEFAULT_FROM_EMAIL = getattr(settings, "DEFAULT_FROM_EMAIL", "")
DEFAULT_TO_EMAIL = getattr(settings, "DEFAULT_TO_EMAIL", "")


class EmailMessage(object):
    def __init__(
        self, email_to, template, subject, context, reply_to=None, email_from=None
    ):
        email_from = email_from or DEFAULT_FROM_EMAIL
        email_to = email_to or DEFAULT_TO_EMAIL

        logger.info(
            "EmailMessage",
            extra={"email_from": email_from, "email_to": email_to, "subject": subject,},
        )

        html_content = render_to_string(template, context)
        msg = EmailMultiAlternatives(subject, html_content, email_from, email_to)
        msg.attach_alternative(html_content, "text/html")
        self.msg = msg

    def send(self):
        self.msg.send()
