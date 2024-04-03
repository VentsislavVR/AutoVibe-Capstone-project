# from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from autovibe_project.carpost.models import CarPost
#
# UserModel = get_user_model()
#
#
# @receiver(post_save, sender=UserModel)
# def user_created(sender, instance, created, **kwargs):
#     if not created:
#         return
#
#
#     CarPost.objects.create(user=instance)