from django.db import models
from authentication.models import User


def uploadTo(instance, filename):
    return 'employees/%s/%s' % (instance.user.username, filename)

# Create your models here.
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='admin')
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=uploadTo, blank=True)
    thumbnail = models.URLField(blank=True)