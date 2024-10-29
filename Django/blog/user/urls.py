from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import profile_view
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view( template_name = 'login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    

]