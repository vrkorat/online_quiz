from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<num>[0-9]+)/$',views.list,name='list'),
]