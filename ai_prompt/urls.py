from django.urls import path
from . import views

urlpatterns = [
    path("", views.evolution_view),
]