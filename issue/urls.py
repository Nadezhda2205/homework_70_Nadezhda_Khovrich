from django.urls import path
from issue.views import TaskListView, TaskDetailView, TaskUpdateView, TaskAddView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('detail/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('add/', TaskAddView.as_view(), name='task_add'),

]
