from django.contrib import admin
from .models import *
# Register your models here.


class noteAdmin(admin.ModelAdmin):
	list_display = ('title', 'note', 'date')

admin.site.register(note, noteAdmin )
