from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = '[account]'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='user_register')

]