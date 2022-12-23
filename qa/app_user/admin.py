from django.contrib import admin

from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(MyUser, MyUserAdmin)