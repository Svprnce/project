from django.urls import path
from app import views

urlpatterns =[
    path('', views.index, name='index'),
    path('view/', views.view, name='viewlist')
]