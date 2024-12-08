import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    can_create_user=models.BooleanField(default=False)
    can_assign_task=models.BooleanField(default=False)
    is_empolyee=models.BooleanField(default=False)
    is_electrician=models.BooleanField(default=False)
    class Meta:
        permissions = [
            ("can_assign_task", "Can assign tasks to users"),
        ]

    def save(self, *args, **kwargs):
        self.name = self.name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name





class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model with additional fields
    """

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
  # Profile picture field

    user_type = models.ForeignKey(
        UserType, on_delete=models.CASCADE, null=True,blank=True, related_name="custom_user_type"
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_password_created = models.BooleanField(default=False)
    forget_password_secret = models.CharField(max_length = 128 ,blank=True, null=True)
    forget_password_secret_expire_time = models.DateTimeField(null= True,blank=True)
   

    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.user_type:
            self.user_type = self.user_type


class Task(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    )
    
    # PRIORITY_CHOICES = (
    #     ('low', 'Low'),
    #     ('medium', 'Medium'),
    #     ('high', 'High'),
    # )
    sr_no=models.CharField(max_length=30)
    # title = models.CharField(max_length=200)
    job_description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    # priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')
    assigned_to = models.CharField(max_length=100,null=True,blank=True)
    assigned_by = models.CharField(max_length=100,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    materials_required = models.TextField(blank=True, null=True) 
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_description

    class Meta:
        ordering = ['-created_at']

class TaskAction(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='actions')
    performed_by = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    action_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.performed_by} - {self.action_description[:50]}"

    class Meta:
        ordering = ['-timestamp']

