from personal_main import views

from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
                       url(r'^$', views.about, name='about'),
                       url(r'^blog/$', include('personal_blog.urls', namespace='personal_blog')))
