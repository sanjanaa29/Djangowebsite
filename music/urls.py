from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^albums/create$',create,name='create'),
    url(r'^$', index,name='index'),
    #path('<int:album_id>', views.detail, name='detail')
]