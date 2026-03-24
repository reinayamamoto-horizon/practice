from django.urls import path
from . import views

app_name = 'evolution_prompt'

urlpatterns = [
    path('evolution/', views.evolution, name='evolution'),
    path('character/', views.character, name='character'),
    path('job/', views.job, name='job'),
]
