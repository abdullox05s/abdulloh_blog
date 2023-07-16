from django.urls import path

from .views import *


urlpatterns=[
    path('index/', index),
    path('portfolio/<int:a>/', portfolio_detail),
    path('single/<int:a>/',single),
    path('mission_single/<int:a>/',mission_single),
    path('my_life/<int:a>/',my_life),
]