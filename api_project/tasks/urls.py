from django.urls import path
from .views import TaskListCreateView, TaskRetriveUpdateDestroyView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('task/<int:pk>/', TaskRetriveUpdateDestroyView.as_view(), name='task-detail'),
]
