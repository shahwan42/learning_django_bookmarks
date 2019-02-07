from django.urls import path, include
from . import views

urlpatterns = [
    # include auth all url paths instead of defining them manually
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('edit/', views.edit, name='edit'),
    path('users/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),  # order matters, this is more specific
    path('users/<username>/', views.user_detail, name='user_detail'),  # this is generic. comes last
]
