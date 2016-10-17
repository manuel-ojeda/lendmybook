from django.contrib import admin
from .models import BaseBook

class BaseBookAdmin(admin.ModelAdmin):
	pass

admin.site.register(BaseBook,BaseBookAdmin)