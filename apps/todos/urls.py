from django.urls import path

from . import views


urlpatterns = [
    path('', views.todo, name='todo'),
    path('task/create/', views.create_task, name='create_task'),
    path('topic/create/', views.create_topic, name='create_topic'),
]
