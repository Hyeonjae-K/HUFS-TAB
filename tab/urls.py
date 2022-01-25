from django.urls import path

from tab import views

urlpatterns = [
    path('board/', views.board),
]
