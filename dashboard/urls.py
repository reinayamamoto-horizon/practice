from django.urls import path
from . import views
from .views import (
    TodoListView,
    TodoCreateView,
    TodoEditView,
    TodoDeleteView,
)


app_name = "dashboard"
urlpatterns = [
    path('<int:user_id>/', views.EXP_bar,name="EXP_bar"),
    path('list/', TodoListView.as_view(), name='todo_list'),
    path('create/<int:character_id>/', TodoCreateView.as_view(), name='todo_create'),
    path('edit/<int:todo_id>/', TodoEditView.as_view(), name='todo_edit'),
    path('delete/<int:todo_id>/', TodoDeleteView.as_view(), name='todo_delete'),

]
