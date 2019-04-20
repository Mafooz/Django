from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views
app_name='Discussion'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^(?P<pk>\d+)/$',views.post_details,name='post_details'),
	url(r'^Post_it/',views.Post_it,name='Post_it'),
]