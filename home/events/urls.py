from django.contrib import admin
from django.urls import path, include
from . import views
from .views import about, events, addPost, updatePost, deletePost, addCategory, categoryView, categoryListView
# from django.conf.urls import url

urlpatterns = [
    path('', events.as_view(), name='events'),
    # path('events/', events.as_view(), name='events'),
    path('addpost/', addPost.as_view(), name='addpost'),
    path('<str:slug>-edit', updatePost.as_view(), name='updatepost'),
    path('<str:slug>-delete', deletePost.as_view(), name='deletepost'),
    path('addcategory', addCategory.as_view(), name='addcategory'),
    path('category/<str:cats>', categoryView, name='category'),
    path('category-list', categoryListView, name='category-list'),
    # path('', views.events, name='events'),
    # path('events', views.events, name='events'),
    path('about/', views.about, name='about'),
    # path('about/', about.as_view(), name='about'),
    # path('addPost', views.addPost, name='addpost'), 
    # path('search', views.search, name='search'),
    path('<str:slug>', views.eventPost, name='eventpost'),
    
    # path('<str:slug>', views.category_list, name='category_list'),
    # url(r'^category$', views.category_list, name='category_list'),
    # url(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
]