from django.contrib import admin

# Register your models here.

from osoby import models


admin.site.register(models.Klasa)
admin.site.register(models.Absolwent)

