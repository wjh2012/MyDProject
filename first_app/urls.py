from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('AGGORA/', views.AGGORA, name='AGGORA'),
    path('AGORA/', views.AGORA, name='AGORA'),
    path('honor/', views.honor, name='honor'),
    path('QnA/', views.QnA, name='QnA'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]