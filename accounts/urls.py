from django.urls import path
from accounts.view import LoginView, logout_view

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('login/', logout_view, name='logout'),
   
]
