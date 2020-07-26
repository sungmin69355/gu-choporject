from django.db import models
from accounts.models import User

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photo = models.ImageField()
    content = models.CharField(max_length=4000)
    published = models.DateTimeField(auto_now=True)
    weather = models.CharField(max_length=15)
    emotion = models.CharField(max_length=15)
    timeout = models.IntegerField(default=0)

    def __str__(self):
        return "%s - %s" % (self.username, self.title)