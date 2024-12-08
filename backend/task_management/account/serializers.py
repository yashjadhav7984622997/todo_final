from django.conf import settings
import os
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password,check_password

class InviteUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=False, allow_blank=True)
    user_type = serializers.PrimaryKeyRelatedField(queryset=UserType.objects.all(), required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'username', 'user_type', 'is_deleted']

    def validate(self, attrs):
        # Get the user who is creating this invitation
        creating_user = self.context['request'].user
        
        # Check if the creating user has permission to create users with the specified user_type
        if not creating_user.user_type.can_create_user:
            raise serializers.ValidationError(
                "You don't have permission to create new users."
            )

        return attrs

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_username(self, value):
        if value and CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def create(self, validated_data):
        # Generate a random password
        password = BaseUserManager().make_random_password(
            length=12, 
            allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        )

        # Create the user
        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            username=validated_data.get('username', None),
            user_type=validated_data['user_type'],
            is_active=True,
            is_password_created=False,
        )
        user.set_password(password)
        user.save()

        # HTML content for the email
        html_content = f"""
        <html>
        <body>
            <h2>Welcome to Our Platform!</h2>
            <p>Hello {user.first_name or user.username or "User"},</p>
            
            <p>You have been invited to join our platform. Here are your login credentials:</p>
            
            <p><strong>Email:</strong> {user.email}<br>
            <strong>Password:</strong> {password}</p>
            
            <p>Please log in and change your password for security purposes.</p>
            
            <p>Best regards,<br>
            The Team</p>
        </body>
        </html>
        """

        # Plain text content for email clients that don't support HTML
        plain_text_content = f"""
        Welcome to Our Platform!
        
        Hello {user.first_name or user.username or "User"},
        
        You have been invited to join our platform. Here are your login credentials:
        
        Email: {user.email}
        Password: {password}
        
        Please log in and change your password for security purposes.
        
        Best regards,
        The Team
        """

        # Send invitation email
        send_mail(
            subject="You've been invited!",
            message=plain_text_content,  # Plain text version
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            html_message=html_content,  # HTML version
            fail_silently=False,
        )

        return user


class AddRoleSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    can_create_user = serializers.BooleanField(required=False, default=False)
    can_assign_task = serializers.BooleanField(required=False, default=False)
    is_empolyee = serializers.BooleanField(required=False, default=False)

    class Meta:
        model = UserType
        fields = ['id', 'name', 'can_create_user', 'can_assign_task', 'is_empolyee']

    def validate_name(self, value):
        if UserType.objects.filter(name=value).exists():
            raise serializers.ValidationError("A UserType with this name already exists.")
        return value

    def create(self, validated_data):
        role = UserType.objects.create(
            name=validated_data['name'],
            can_create_user=validated_data.get('can_create_user', False),
            can_assign_task=validated_data.get('can_assign_task', False),
            is_empolyee=validated_data.get('is_empolyee', False),
        )
        return role
    

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'


'''
    user login serializer
'''
class Login_serializers(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)

    class Meta:
        model = CustomUser
        fields = ["email", "password"]


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id','email','username','user_type']
        depth = 1




class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_blank=False,required=True)
 
    def validate(self, attrs):
        errors = {}
 
        email = attrs.get("email")
 
 
 
        if not email:
            errors['email'] = "Email Should not be blank."
 
        if not CustomUser.objects.filter(email = email).exists():
            errors['email'] = f"User does not exist this email {email}"
        secret = ""
        user = CustomUser.objects.filter(forget_password_secret = secret).first()
            
        if errors:
            raise serializers.ValidationError()
 
        return attrs
 


class UserResetPasswordSerializer(serializers.Serializer):
    secret = serializers.CharField(allow_blank=True)
    new_password = serializers.CharField(allow_blank=True)
    new_confirm_password = serializers.CharField(allow_blank=True)
 
    def validate(self, attrs):
        errors = {}
        secret = attrs.get("secret")
        new_password = attrs.get("new_password")
        new_confirm_password = attrs.get("new_confirm_password")
        
        if not new_password:
            errors['new_password'] = "New password cannot be blank."
 
        if not new_confirm_password:
            errors['new_confirm_password'] = "New confirm password cannot be blank."
 
        if new_confirm_password != new_password:
            errors['new_confirm_password'] = "New confirm password and New password do not match."
 
        if not CustomUser.objects.filter(forget_password_secret=secret).exists():
            errors['secret'] = "Secret not valid."
            
        if errors:
            raise serializers.ValidationError(errors)
 
        return attrs
 
    def update(self, instance, validated_data):
        new_password = validated_data.get("new_password")
        print(f"old password{instance.password}")
        is_correct = check_password(new_password, instance.password)
        
        # Set the new password and save the instance
        instance.password=make_password(new_password)
        instance.forget_password_secret = ""
        instance.save()
        print(instance.password)
        
        return instance


# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'

#     def create(self, validated_data):
#         task = Task.objects.create(**validated_data)
#         return task

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.status = validated_data.get('status', instance.status)
#         instance.priority = validated_data.get('priority', instance.priority)
#         instance.assigned_to = validated_data.get('assigned_to', instance.assigned_to)
#         instance.location = validated_data.get('location', instance.location)
#         instance.due_date = validated_data.get('due_date', instance.due_date)
#         instance.save()
#         return instance
class TaskSerializer(serializers.ModelSerializer):
    assigned_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority',
            'assigned_to', 'assigned_by', 'location', 'deadline',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, attrs):
        user = self.context['request'].user
        
        # Check if user has permission to assign tasks
        if not user.user_type.can_assign_task:
            raise serializers.ValidationError(
                "You don't have permission to create or assign tasks."
            )

        # Validate assigned_to user exists and is active
        assigned_to = attrs.get('assigned_to')
        if assigned_to:
            if not assigned_to.is_active:
                raise serializers.ValidationError(
                    {"assigned_to": "Cannot assign task to inactive user."}
                )
            if assigned_to.is_deleted:
                raise serializers.ValidationError(
                    {"assigned_to": "Cannot assign task to deleted user."}
                )

        return attrs

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['assigned_to'] = {
            'id': instance.assigned_to.id,
            'email': instance.assigned_to.email,
            'name': f"{instance.assigned_to.first_name} {instance.assigned_to.last_name}".strip()
        }
        representation['assigned_by'] = {
            'id': instance.assigned_by.id,
            'email': instance.assigned_by.email,
            'name': f"{instance.assigned_by.first_name} {instance.assigned_by.last_name}".strip()
        }
        if instance.location:
            representation['location'] = {
                'id': instance.location.id,
                'name': instance.location.name
            }
        return representation




# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = '__all__'

class TaskActionSerializer(serializers.ModelSerializer):
    performed_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    task = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TaskAction
        fields = ['id', 'task', 'performed_by', 'action_description','materials_required', 'timestamp']
        read_only_fields = ['timestamp', 'task']

    def validate(self, attrs):
        # The task will be set in the view
        return attrs

from rest_framework import serializers
from .models import CustomUser, UserType

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['id', 'name', 'can_create_user', 'can_assign_task', 'is_empolyee']

class UserSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(read_only=True)
    available_user_types = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            'id', 'email', 'first_name', 'last_name', 'full_name',
            'user_type', 'is_active', 'created_at', 'available_user_types'
        ]

    def get_full_name(self, obj):
        return f"{obj.first_name or ''} {obj.last_name or ''}".strip()

    def get_available_user_types(self, obj):
        return UserTypeSerializer(UserType.objects.all(), many=True).data