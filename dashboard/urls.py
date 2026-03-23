from django.urls import path
from . import views


app_name = "dashboard"
urlpatterns = [
    path("", views.EXP_bar,name="EXP_bar"),
]
