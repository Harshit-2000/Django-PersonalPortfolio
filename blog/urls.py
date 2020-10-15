from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_blog, name = 'all_blog'),
    path('<int:blog_id>/', views.details , name = 'details')
]