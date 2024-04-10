from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()

# Todo if i have the time
class Comment(models.Model):
    text = models.TextField(

    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

# Todo if i have the time to implement payment
class CarPostSystemSettings(models.Model):
    MAX_BLOGS_PER_USER = models.IntegerField(
        default=3
    )
