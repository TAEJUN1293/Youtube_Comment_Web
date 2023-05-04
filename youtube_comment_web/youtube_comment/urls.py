from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('detail', views.detail, name='detail')
]