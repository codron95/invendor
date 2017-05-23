from django.contrib import admin
from .models import tripAnalytics,tripGps

# Register your models here.
admin.site.register(tripGps)
admin.site.register(tripAnalytics)