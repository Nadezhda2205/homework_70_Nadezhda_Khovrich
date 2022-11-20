from django.contrib import admin
from django.urls import path, include
from api.views import ProjectAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('issue.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/project/<int:pk>', ProjectAPIView.as_view()),
    path('api/project/', ProjectAPIView.as_view()),
]
