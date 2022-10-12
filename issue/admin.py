from django.contrib import admin
from issue.models import Status, Task, Type, Project

admin.site.register(Status)
admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Project)
