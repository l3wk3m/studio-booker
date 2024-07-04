from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Unavailable"), (1, "Available"))

# Create your models here.
# Artist model extending base user model
class Artist(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
            return f"{self.first_name + ' ' + self.last_name}"

class Studios(models.Model):
    """
    Django database model for studio spaces
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


