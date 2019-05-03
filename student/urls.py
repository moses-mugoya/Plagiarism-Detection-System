from django.urls import re_path
from . import views

app_name = 'student'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^upload/', views.student, name='upload'),
    re_path(r'^student/detail/(?P<id>\d+)/$', views.perform_plagiarism, name='plagiarism'),
]
