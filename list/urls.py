from django.urls import path
from . import views
app_name = "list"

urlpatterns = [
    path("", views.index, name="index"),
    path("clear", views.clear, name="clear"),
    path('save-finished-tasks/', views.save_finished_tasks, name='save_finished_tasks'),
]