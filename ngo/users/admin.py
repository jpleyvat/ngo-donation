from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

class AdminAccount(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_staff')
    search_fields =('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()




# Register your models here.
admin.site.register(Profile)
# admin.site.register(CustomUser, AdminAccount)

admin.site.register(CustomUser)