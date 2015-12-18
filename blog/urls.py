from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^blog/pop/(?P<id>\d+)/$', views.post_detail),
    url(r'^blog/pop/$', views.pop_post),
    url(r'^post/new/$', views.new_post, name='new_post'),
]