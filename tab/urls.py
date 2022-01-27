from os import name
from django.urls import path
from django.contrib.auth import views as auth_views

from tab import views

app_name = 'tab'
urlpatterns = [
    path('board/', views.board, name='board'),
    path('board/detail/<int:content_id>',
         views.board_detail, name='board_detail'),
    path('board/post', views.board_post, name='board_post'),
    path('board/modify/<int:content_id>',
         views.board_modify, name='board_modify'),
    path('board/delete/<int:content_id>',
         views.board_delete, name='board_delete'),
    path('recruiting/', views.recruiting, name='recruiting'),
    path('recruiting/success/', views.recruiting_success,
         name='recruiting_success'),
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='tab/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
