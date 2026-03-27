from django.urls import path
from .views import (
    TodoListView,
    TodoCreateView,
    TodoDetailView,
    TodoEditView,
    TodoDeleteView,
    EXPbarView,
)

app_name = "dashboard"

urlpatterns = [
    path("", EXPbarView.as_view(),name="EXP_bar"),
    path('list/<int:character_id>/', TodoListView.as_view(), name='todo_list'),
    path('create/<int:character_id>/', TodoCreateView.as_view(), name='todo_create'),
    path('detail/<int:todo_id>/', TodoDetailView.as_view(), name='todo_detail'),
    path('edit/<int:todo_id>/', TodoEditView.as_view(), name='todo_edit'),
    path('delete/<int:todo_id>/', TodoDeleteView.as_view(), name='todo_delete'),
]
