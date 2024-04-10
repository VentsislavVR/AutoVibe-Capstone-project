from smtplib import SMTPException

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import BadHeaderError
from django.template.loader import render_to_string
from autovibe_project.settings import EMAIL_HOST_USER

from autovibe_project.accounts.models import Profile

UserModel = get_user_model()


# from django.core.mail import get_connection
# connection = get_connection(
#     host='smtp.gmail.com',
#     port=587,
#     username=EMAIL_HOST_USER,
#     password=EMAIL_HOST_PASSWORD,
#     use_tls=True
# )
# connection.open()
# print(connection)

@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    # created = False, when update
    # create = True, when create
    if not created:
        return

    # Eager save
    print("User created signal received")
    Profile.objects.create(user=instance)
    # send_welcome_email(instance.email)
    # send_mail(
    #     subject='Welcome to AutoVibe',
    #     message='Your account has been created.',
    #     from_email=EMAIL_HOST_USER,
    #     recipient_list=['wibeka1517@kravify.com'],
    #     html_message=render_to_string('email/email-greeting.html', {'email': instance.email}),
    #     fail_silently=False
    # )
    try:
        send_mail(
            subject='Welcome to AutoVibe',
            message='Your account has been created.',
            from_email=EMAIL_HOST_USER,
            recipient_list=[instance.email],
            html_message=render_to_string('email/email-greeting.html', {'email': instance.email}),
            fail_silently=False
        )
    except BadHeaderError:
        print("Invalid header found.")
    except SMTPException as e:
        print("An error occurred:", e)


@receiver(post_save, sender=UserModel)
def save_user(sender, instance, **kwargs):
    post_save.disconnect(save_user, sender=UserModel)
    instance.profile.save()
    post_save.connect(save_user, sender=UserModel)


# def send_welcome_email(email):
#     print("Sending welcome email to:", email)
#     mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY), version='v3.1')
#     html_content = render_to_string('email/email-greeting.html', {'email': email})
#     data = {
#         'Messages': [
#             {
#                 "From": {
#                     "Email": "autovibe@abv.bg",
#                     "Name": "AutoVibe"
#                 },
#                 "To": [
#                     {
#                         "Email": email
#                     }
#                 ],
#                 "Subject": "Welcome to AutoVibe",
#                 "TextPart": "Greetings from AutoVibe",
#                 "HTMLPart": html_content
#             }
#         ]
#     }
#
#     result = mailjet.send.create(data=data)
#     print("Mailjet API Response:", result)
#     print(result.status_code)
#     print(result.json())
#     return result


"""
User created signal received
Sending welcome email to: ventsislav.vichkov.rachev@gmail.com
Mailjet API Response: <Response [401]>
401
{'ErrorIdentifier': '0ff2b195-b772-4b1d-887a-dc49d5da8375', 'ErrorCode': 'mj-0001', 
'StatusCode': 401, 'ErrorMessage':
 'Your account has been temporarily blocked. Please contact our support team to get assistance.'}

TODO fix this
"""
