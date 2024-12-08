from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('profile/', views.profile, name='profile'),
    # path('notifications/', views.notifications_view, name='notifications'),
    path('search/', views.search, name='search'),
    path('calendar/', views.calendar, name='calendar'),
    path('api/tasks/calendar/', views.calendar_events, name='calendar_events'),
    path('analytics/', views.analytics, name='analytics'),
    # User Management URLs
    path('users/', views.user_management, name='user_management'),
    
    # API endpoints
    path('api/users/', views.user_api, name='user_api'),
    path('api/users/<int:user_id>/', views.user_detail_api, name='user_detail_api'),
    
    path('tasks/<int:pk>/update-status/', views.task_status_update, name='task_status_update'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # User management URLs
    path('users/', views.user_management, name='user_management'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:user_id>/edit/view/', views.user_edit_view, name='user_edit_view'),
    path('users/<int:user_id>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:user_id>/delete/view/', views.user_delete_view, name='user_delete_view'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    # Task deletion URLs
    path('users/<int:user_id>/update/', views.update_user, name='update_user'),

    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    # path('api/tasks/<int:task_id>/delete/', views.TaskDeleteAPI.as_view(), name='task_delete_api'),

    # ... your existing API URLs ...
    path('download-completed-tasks/', views.download_completed_tasks, name='download_completed_tasks'),
]