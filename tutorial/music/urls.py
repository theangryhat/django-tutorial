from django.conf.urls import url include
import .views
from django.contrib import admin


urlpattterns = [
    path('', views.index,name='index'),
]
