from django.contrib import admin
from .models import request,hospital,user

# Register your models here.
admin.site.register(request)
admin.site.register(user)
admin.site.register(hospital)
