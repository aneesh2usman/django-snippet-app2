from django.db import models
from django.contrib.auth import get_user_model
class Tags(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Snippets(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True
    )
    title = models.CharField(max_length=50)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags,blank=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['created']
