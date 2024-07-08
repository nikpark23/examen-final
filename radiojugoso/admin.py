from django.contrib import admin
from .models import Genero, Alumno  
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User




# Register your models here.
admin.site.register(Genero)
admin.site.register(Alumno)



class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)