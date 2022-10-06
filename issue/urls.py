from django.urls import path
from issue.views import TaskListView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('detail/<int:pk>', TaskDetailView.as_view(), name='task_detail'),

]
