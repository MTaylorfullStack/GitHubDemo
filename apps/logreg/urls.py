from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^add_message$', views.add_message),
    url(r'^like/(?P<id>\d+)$', views.like)
]