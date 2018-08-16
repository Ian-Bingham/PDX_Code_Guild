from django.urls import path
from . import views

app_name = 'todo_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('markdone/<int:todo_id>', views.markdone, name='markdone'),
]
