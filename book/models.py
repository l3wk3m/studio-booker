from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Unavailable"), (1, "Available"))

# Create your models here.
# Artist model extending base user model
class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_phone = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
            return f"{self.first_name + ' ' + self.last_name + ', username: ' + self.user}"

class Studio(models.Model):
    """
    Django database model for studio spaces
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    availability = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.name

class StudioBooking(models.Model):
    """
    Django database model for available studios
    """
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        formatted_start_time = self.start_time.strftime('%Y-%m-%d %H:%M')
        return f"{self.studio.name} - {formatted_start_time}"
