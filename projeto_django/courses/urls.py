from django.conf.urls import patterns, include, url

urlpatterns = patterns('projeto_django.courses.views',
    url(r'^$', 'index', name='index'),
)
