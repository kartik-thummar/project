from django.contrib import admin
from django.urls import path, include
from . import views
# from django.conf.urls import url

urlpatterns = [
    path('', views.events, name='events'),
    path('events', views.events, name='events'),
    path('about', views.about, name='about'), 
    # path('search', views.search, name='search'),
    # path('<str:slug>', views.eventPost, name='eventpost'),
    # path('<str:slug>', views.category_list, name='category_list'),
    # url(r'^category$', views.category_list, name='category_list'),
    # url(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
]