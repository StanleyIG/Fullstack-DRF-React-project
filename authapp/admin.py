from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authapp.forms import CustomUserCreationForm
from authapp.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", 'first_name', 'last_name', "password1", "password2", "is_superuser", "is_staff"),
        }),
    )
    list_display = ["id", "username", "email", "is_active", "date_joined"]
    ordering = ["-date_joined"]
    readonly_fields = ["date_joined"]