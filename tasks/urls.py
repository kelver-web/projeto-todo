from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasklist),
    path('newtask/', views.newtask),
    path('task/<int:id>/', views.taskView),
    path('edit/<int:id>/', views.edittask),
    path('changestatus/<int:id>/', views.changestatus),
    path('delete/<int:id>/', views.deletetask),
]
