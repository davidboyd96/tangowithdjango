from django.conf.urls import patterns, url, include
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', include('about.urls'))
                       )
