from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomerUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomerUser
    list_display = ['username', 'email', 'birth_day', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birth_day',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('birth_day',)}),
    )


admin.site.register(CustomerUser, CustomUserAdmin)
