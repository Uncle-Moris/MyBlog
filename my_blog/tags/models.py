from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.slug}"
