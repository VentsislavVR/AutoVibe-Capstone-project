from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()


class Comment(models.Model):
    text = models.TextField(

    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    from django.db import models


# Todo
class CarPostSystemSettings(models.Model):
    MAX_BLOGS_PER_USER = models.IntegerField(
        default=3
    )
