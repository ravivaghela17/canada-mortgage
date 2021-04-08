from django.conf.urls import url, include
from django.urls import path
from blog_app import views
urlpatterns = [
    url(r'^$', views.blogs, name="all_blogs"),
    path('<slug:slug>', views.getBlog, name='blog_post'),
]
