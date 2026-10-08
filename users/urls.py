from django.urls import path
from .views import RegisterView, email_verification
from django.contrib.auth.views import LogoutView, LoginView


app_name = 'users'

urlpatterns = [
    path('register_users/', RegisterView.as_view(), name='register_users'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/product_list/'), name='logout'),
    path('email_confirm/<str:token>/', email_verification, name='email_confirm'),
]
