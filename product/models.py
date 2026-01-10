from io import BytesIO
from typing import Any

from django.conf import settings
from django.core.files import File
from django.db import models
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return f"/{self.slug}/"


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploads/", blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return f"/{self.category.slug}/{self.slug}/"

    def _get_base_url(self) -> str:
        """Return base URL from settings or default to localhost."""
        return str(getattr(settings, "BASE_URL", "http://127.0.0.1:8000"))

    def _get_field_url(self, field: Any) -> str:
        """Safely extract URL from ImageFieldFile."""
        if field:
            url = getattr(field, "url", None)
            if url:
                return str(url)
        return ""

    def get_image(self) -> str:
        if self.image_url:
            return self.image_url
        field_url = self._get_field_url(self.image)
        if field_url:
            return f"{self._get_base_url()}{field_url}"
        return ""

    def get_thumbnail(self) -> str:
        if self.image_url:
            return self.image_url
        field_url = self._get_field_url(self.thumbnail)
        if field_url:
            return f"{self._get_base_url()}{field_url}"
        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            thumb_url = self._get_field_url(self.thumbnail)
            if thumb_url:
                return f"{self._get_base_url()}{thumb_url}"
        return ""

    def make_thumbnail(self, image: Any, size: tuple[int, int] = (300, 200)) -> File:
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
