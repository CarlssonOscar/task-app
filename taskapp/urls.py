from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('addtask', views.addTask, name='addtask'),
    path('finished/<task_id>', views.finishedTask, name='finished'),
    path('deletefinsihed', views.deleteFinished, name='deletefinished'),
    path('delete', views.delete, name='delete'),
]