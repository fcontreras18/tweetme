from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Tweet(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    content     = models.CharField(max_length=140)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

def clean(self, *args, **kwargs):
    content self.content
    if content == "abc":
        raise ValidationError("Cannot be ABC")
    return super(Tweet, self)clean(*args, **kwargs)