from django.contrib import admin
from .models import UserIP

class UserIPAdmin(admin.ModelAdmin):
	list_display = ('host_name',)

admin.site.register(UserIP, UserIPAdmin)
