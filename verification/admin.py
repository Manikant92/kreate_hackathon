from django.contrib import admin
from .models import CustomerData,DOBMatch,NameMatch

# Register your models here.
admin.site.register(CustomerData)
admin.site.register(DOBMatch)
admin.site.register(NameMatch)