from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import CustomUser, UserType,  Task, TaskAction

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username',  'user_type')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username',  'user_type')

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = (
        "email",
        "first_name",
        "last_name",
        "username",
       
        "user_type",
        "is_active",
        "is_staff",
    )
    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
        "user_type",
    )

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "username",  "user_type")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser","groups","user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "first_name", "last_name",
                "username",  "user_type", "is_active", "is_staff",
                "is_superuser","groups","user_permissions",
            ),
        }),
    )

    search_fields = ("email", "first_name", "last_name", "username")
    ordering = ("email",)

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'can_create_user', 'can_assign_task', 'is_empolyee')
    list_filter = ('can_create_user', 'can_assign_task', 'is_empolyee')

# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ( 'assigned_to', 'assigned_by', 'deadline', 'status')
    list_filter = ('status', 'created_at', 'deadline')
    
    date_hierarchy = 'created_at'

@admin.register(TaskAction)
class TaskActionAdmin(admin.ModelAdmin):
    list_display = ('task', 'performed_by', 'action_description', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('action_description',)
    date_hierarchy = 'timestamp'

# Register the models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserType, UserTypeAdmin)
