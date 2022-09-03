from django.contrib import admin
from .models import CrudModel

# Register your models here.
class CrudAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(CrudModel, CrudAdmin)
