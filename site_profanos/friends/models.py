from django.db import models
from django.utils.text import slugify

class Friend(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/')
    password_hash = models.CharField(max_length=128)
    password_hint = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
