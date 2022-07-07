from django.contrib import admin
from . import models

admin.site.register(models.Cource)
admin.site.register(models.cource_user)
admin.site.register(models.tags)
admin.site.register(models.cart)
admin.site.register(models.comment)
admin.site.register(models.my_cources)

