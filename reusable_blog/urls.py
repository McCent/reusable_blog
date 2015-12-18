from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reusable_blog/$', views.post_list, name='post_list'),
    url(r'^reusable_blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^reusable_blog/pop/(?P<id>\d+)/$', views.post_detail),
    url(r'^reusable_blog/pop/$', views.pop_post),
    url(r'^post/new/$', views.new_post, name='new_post'),
]