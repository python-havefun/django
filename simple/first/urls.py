from django.conf.urls import url

from . import views

app_name='first'
urlpatterns=[
    url(r'^$',views.details,name='details'),
    url(r'^(?P<question_id>[0-9]+)/$',views.index,name='index'),
    url(r'^user$',views.user_data,name='index'),
    url(r'^search-form/$',views.search_form,name='search-form'),
    url(r'^search/$',views.search),
    ]
