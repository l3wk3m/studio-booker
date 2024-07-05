from django.contrib import admin
from .models import Artist, Studio, StudioBooking

# Register your models here.
admin.site.register(Artist)
admin.site.register(Studio)
admin.site.register(StudioBooking)