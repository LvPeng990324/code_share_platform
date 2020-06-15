from django.contrib import admin
from . import models


@admin.register(models.TestCode)
class TestCodeInformation(admin.ModelAdmin):
    list_display = ('title', 'status', 'remark')

