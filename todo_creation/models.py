from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    date = models.DateField()
    status = models.BooleanField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
