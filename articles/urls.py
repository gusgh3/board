from django.urls import path
from . import views #현재 폴더와 같은 위치에서 가져옴 그래서 . 사용

urlpatterns = [
    path('', views.index), 
]