from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/', views.upload_file_csv, name='upload'),
    url(r'^post/(?P<id>\d+)/', views.post, name='post'),
]