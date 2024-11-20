
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('index/', views.index, name= 'index'),
    path('service/', views.services, name= 'services'),
    path('starter/', views.starter, name= 'starter'),
    path('about/', views.about, name= 'about'),
    path('doctors/', views.doctors, name= 'doctors'),
    path('myservice/', views.myservice, name= 'myservice'),
    path('appointment/', views.appointment, name= 'appointment'),
    path('comment/', views.comment, name= 'comment'),
    path('show/', views.show, name= 'show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
]
