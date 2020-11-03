from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_post, name='group'),
    path('new_post/', views.new_post, name='new_post'),


    path('profile/<str:username>/', views.profile, name='profile'),
    path('<str:username>/<int:post_id>/', views.post_view, name='post'),

    path('<str:username>/<int:post_id>/edit/',
         views.post_edit, name='post_edit'),

   path('profile/<str:username>/', views.profile, name='profile'),
    path('<str:username>/<int:post_id>/', views.post_view, name='post'),

   path('<str:username>/<int:post_id>/edit/', views.post_edit, name='post_edit'),



]
