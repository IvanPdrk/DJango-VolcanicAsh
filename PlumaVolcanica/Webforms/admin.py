#DJango
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#Models
from django.contrib.auth.models import User

#Models
#from Webforms.models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user')
    list_filter = ('created','modified')

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
