from django.urls import path

from . import views

urlpatterns = [
    path('', views.allBlogs, name='all_blogs'),
    path('<int:blog_id>', views.details, name='details')
]
