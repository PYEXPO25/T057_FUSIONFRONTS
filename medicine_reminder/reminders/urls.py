from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-reminder/', views.add_reminder, name='add_reminder'),
    path('logout/', views.logout_view, name='logout'),
]