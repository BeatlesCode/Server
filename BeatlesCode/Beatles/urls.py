from django.urls import path
from . import views #.은 현재폴더의 디렉토리라는뜻. 즉 현재폴더의 views.py를 import하는것임

urlpatterns = [
path('', views.index, name='index'),
path('index_upload/', views.index_upload, name='index_upload'),
path('output.html', views.output, name='output'),
]