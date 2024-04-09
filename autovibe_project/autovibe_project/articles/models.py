from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from cloudinary import models as cloudinary_models

UserModel = get_user_model()
class Article(models.Model):
    MAX_NAME_LENGTH = 30

    MAX_CONTENT_LENGTH = 10000

    slug = models.SlugField(
        editable=False,
        unique=True,
        null=False,
        blank=True
    )
    name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )
    article_img = cloudinary_models.CloudinaryField(
        "articles",
        blank=True,
        null=True
    )

    content = models.TextField(
        max_length=MAX_CONTENT_LENGTH
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    class Meta:
        permissions = [
            ("can_change_article", "Can change article"),
            ("can_add_article", "Can add article"),
            ("can_delete_article", "Can delete article"),
        ]


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


