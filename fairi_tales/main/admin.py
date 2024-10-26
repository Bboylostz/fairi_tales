from django.contrib import admin

from . import models

admin.site.register(models.Story)
admin.site.register(models.Genre)
admin.site.register(models.Autor)