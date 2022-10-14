from issue.models import Task, Project
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description',  'status',  'type', 'project']


class SearchTaskForm(forms.Form):
    search = forms.CharField(required=False)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']

