from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User
from django import forms
from django.core.exceptions import ValidationError


# TODO: ここを変更
class MyUserChangeForm(UserChangeForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password", "is_superuser", "is_staff"]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        # ("Important Dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    list_display = [
        "email",
        "is_staff",
        "is_superuser",
        "created_at",
        "updated_at",
        "last_login",
    ]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    search_fields = ["email"]
    ordering = [
        "email",
    ]
    filter_horizontal = []
