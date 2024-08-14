from unittest import TestCase
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from invoicepro.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

class EmailTestCase(TestCase):
    def setUp(self) -> None:
        settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        settings.EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
        settings.EMAIL_HOST_USER = EMAIL_HOST_USER
        settings.EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
        settings.EMAIL_PORT = '2525'
    
    def test_sending_mail(self):
        subject = 'Test subject email'
        html_message = render_to_string('estimates/mail_template.html', {'context': 'values'})
        plain_message = strip_tags(html_message)
        from_email = 'from@yourdjangoapp.com'
        to = 'to@yourbestuser.com'

        message = EmailMessage(subject=subject, body=plain_message, from_email=from_email, to=(to, ))
        message.send()

