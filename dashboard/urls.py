from django.urls import path
from . import views
from .views import (
    TodoListView,
    TodoCreateView,
    TodoDetailView,
    TodoEditView,
    TodoDeleteView,
    IndexView,
    TodoCompleteView,
)

app_name = "dashboard"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('list/', TodoListView.as_view(), name='todo_list'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path('detail/<int:todo_id>/', TodoDetailView.as_view(), name='todo_detail'),
    path('edit/<int:todo_id>/', TodoEditView.as_view(), name='todo_edit'),
    path('delete/<int:todo_id>/', TodoDeleteView.as_view(), name='todo_delete'),
    path("complete/<int:todo_id>/", TodoCompleteView.as_view(), name="todo_complete"),
]
