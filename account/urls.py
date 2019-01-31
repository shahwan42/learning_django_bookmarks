from django.urls import path, include
from . import views

urlpatterns = [
    # include auth all url paths instead of defining them manually
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('edit/', views.edit, name='edit'),
]
