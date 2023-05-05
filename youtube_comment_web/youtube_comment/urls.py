from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('detail', views.detail, name='detail'),
    path('load/video/', views.PostVideo.as_view()),
    path('load/comment/', views.PostComment.as_view()),
    path('load/keyword/', views.PostKeyword.as_view()),
]