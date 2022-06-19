from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('tags.Tag', related_name='posts')

    def __str__(self):
        return f'{self.id} {self.title}'