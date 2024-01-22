from django.db import models
from datetime import datetime

# Create your models here.
class Guestbook(models.Model):
    idx = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=50)
    name = models.CharField(null=False, max_length=50)
    email = models.CharField(null=False, max_length=50)
    passwd = models.CharField(null=False, max_length=50)
    content = models.TextField(null=False)
    post_date = models.DateTimeField(default=datetime.now, blank=True)