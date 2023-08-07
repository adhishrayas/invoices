from django.contrib import admin
from .models import Invoice,Invoice_Detail
# Register your models here.
admin.site.register(Invoice)
admin.site.register(Invoice_Detail)