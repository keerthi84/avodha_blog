from django.urls import path
from . import views
from .views import home,article_view,addpost,updatepost,deletepost

urlpatterns = [
    path('',home.as_view(),name='home'),
    path('article/<int:pk>/',article_view.as_view(),name='dview'),
    path('addpost/',addpost.as_view(),name='add'),
    path('article/edit<int:pk>/',updatepost.as_view(),name='update'),
    path('delete/<int:pk>',deletepost.as_view(),name='delete'),


]