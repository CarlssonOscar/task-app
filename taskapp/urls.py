from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('addtask', views.add_task, name='addtask'),
    path('finished/<task_id>', views.finished_task, name='finished'),
    path('deletefinsihed', views.delete_finished, name='deletefinished'),
    path('clear', views.clear, name='clear'),
]
