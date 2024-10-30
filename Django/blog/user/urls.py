# django
from django.urls import path
from django.contrib.auth import views as auth_views

# rest framework
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from . import views
from .views import LogoutView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view( template_name = 'login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/', LogoutView.as_view(), name='token_logout')

]
