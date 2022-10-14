from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from typing import Any
from issue.forms import TaskForm, SearchTaskForm
from issue.models import Task
from django.urls import reverse
from django.db.models import Q


class TaskListView(ListView):
    template_name: str = 'task_list.html'
    model = Task
    context_object_name = 'tasks'
    paginate_by = 3
    paginate_orphans = 1

 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchTaskForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(summary__iregex=self.search_value) | Q(description__iregex=self.search_value)
                )
        return queryset


class TaskDetailView(DetailView):
    template_name: str = 'task_detail.html'
    model = Task
    context_object_name = 'task'


class TaskUpdateView(TemplateView):
    template_name: str = 'task_update.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(instance=task)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form: TaskForm = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
        context = {
            'form': form
        }
        return render(request, 'task_update.html', context)
   

class TaskCreateView(CreateView):
    template_name: str = 'task_create.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})



class TaskDeleteView(TemplateView):
    template_name: str = 'task_delete.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()       
        return redirect('task_list')
