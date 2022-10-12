from issue.models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description',  'status',  'type']


class SearchTaskForm(forms.Form):
    search = forms.CharField(required=False)