from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name='show_index'),
    path('<title>/', views.show_code, name='show_code'),
]
