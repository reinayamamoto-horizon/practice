from django.urls import path
from . import views

app_name = 'ai_prompt'

urlpatterns = [
    path('evolution/', views.evolution, name='evolution'),
]
