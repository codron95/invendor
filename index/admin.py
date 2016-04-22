from django.contrib import admin
from index.models import subscribers,queries,expense

# Register your models here.
admin.site.register(subscribers)
admin.site.register(queries)
admin.site.register(expense)