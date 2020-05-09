from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('London', views.index),
    path('New York', views.index),
    path('Gallifrey', views.index)

]
