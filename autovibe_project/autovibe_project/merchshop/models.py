from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.validators import MinLengthValidator
from django.db import models
from django.template.defaultfilters import slugify
from io import BytesIO
from PIL import Image
from cloudinary import models as cloudinary_models
UserModel = get_user_model()
# Create your models here.
class TitleSlugMixin(models.Model):
    TITLE_MAX_LENGTH = 255
    SLUG_MAX_LENGTH = 255

    TITLE_MIN_LENGTH = 1
    SLUG_MIN_LENGTH = 1

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(TITLE_MIN_LENGTH),

        ]
    )
    slug = models.SlugField(
        max_length=SLUG_MAX_LENGTH,
        null=False,
        blank=False,
        unique=True,
        validators=[
            MinLengthValidator(SLUG_MIN_LENGTH),
        ]
    )

    def save(self, *args, **kwargs):
        # Generate unique slug based on product name
        if not self.slug:
            self.slug = slugify(self.name)
            counter = 1
            while Product.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.name)}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class Product(TitleSlugMixin):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    description = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    date_added = models.DateTimeField(
        auto_now_add=True
    )
    image = cloudinary_models.CloudinaryField(
        'merch_items',
        blank=True,
        null=True
    )
    thumbnail = cloudinary_models.CloudinaryField(
        'merch_items',
        blank=True,
        null=True
    )


    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail
            else:
                return 'https://via.placeholder.com/240x180.png'
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-date_added']


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'