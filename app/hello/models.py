from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year_published = models.IntegerField()
    registration_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10) # This can be changed to a choices field for specific statuses
    tags = models.ManyToManyField(Tag, related_name='books', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
