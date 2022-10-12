from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from typing import Any
from issue.forms import TaskForm, SearchTaskForm
from issue.models import Task
from django.db.models import Q


class TaskListView(ListView):
    template_name: str = 'task_list.html'
    model = Task
    context_object_name = 'tasks'
    paginate_by = 3
    paginate_orphans = 1

 
    def get_context_data(self, **kwargs):
        print('get_context_data')

        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def get(self, request, *args, **kwargs):
        print('get')

        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        print(self.search_value)
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        print('get_search_form')
        return SearchTaskForm(self.request.GET)

    def get_search_value(self):
        print('get_search_value')

        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        print('get_queryset')
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(summary__iregex=self.search_value) | Q(description__iregex=self.search_value)
                )
        return queryset


class TaskDetailView(TemplateView):
    template_name: str = 'task_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


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


class TaskAddView(TemplateView):
    template_name: str = 'task_add.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        form = TaskForm()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form: TaskForm = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
        context = {
            'form': form
        }
        return render(request, 'task_add.html', context)


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
