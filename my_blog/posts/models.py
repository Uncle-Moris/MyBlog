from django.db import models
from main.models import Timestamped


class Post(Timestamped):
    title = models.CharField(max_length=250)
    content = models.TextField()
    tags = models.ManyToManyField('tags.Tag', related_name='posts')

    def __str__(self):
        return f'{self.id} {self.title}'
