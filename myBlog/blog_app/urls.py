from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^post_detail/(?P<pk>[0-9]+)$', views.single_post, name='single_post'),
    url(r'^post_detail/(?P<pk>[0-9]+)/update$', views.PostUpdate.as_view(), name='update')
]