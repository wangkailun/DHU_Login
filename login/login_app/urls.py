from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('check_user/', views.check_user, name="checkUser"),
    path('add_user/', views.add_user, name="addUser"),
]
