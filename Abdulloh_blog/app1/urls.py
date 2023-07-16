from django.urls import path

from .views import *

urlpatterns=[
    path('blog/',blog),
    path('blog-single/<int:a>/', blog_single),
    path('blog_filter/<int:a>/',blog_filter),
    path('blog_tag/<int:a>/',blog_tag)


]