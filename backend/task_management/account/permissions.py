from rest_framework.permissions import BasePermission

class CanCreateUser(BasePermission):
    def has_permission(self, request, view):
        # Check if user is authenticated and has a user_type with can_create_user permission
        return (
            request.user.is_authenticated and 
            request.user.user_type and 
            request.user.user_type.can_create_user
        ) 
from rest_framework.permissions import BasePermission

class CanAssignTask(BasePermission):
    def has_permission(self, request, view):
        # Allow read operations for all authenticated users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
            
        # Check if user has permission to assign tasks
        return (
            request.user.is_authenticated and 
            request.user.user_type and 
            request.user.user_type.can_assign_task
        )

class IsEmployeeAssignedToTask(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.user_type and 
            request.user.user_type.is_empolyee
        )

    def has_object_permission(self, request, view, obj):
        # Check if user is assigned to this task
        return obj.assigned_to == request.user