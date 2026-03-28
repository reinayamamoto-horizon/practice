from django.urls import path
from .views import Login, Signup, Logout
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("signup/", Signup.as_view(), name="signup"),
    path("logout/", Logout.as_view(), name="logout"),
]