from django.conf.urls import url include
import .views
from django.contrib import admin


urlpattterns = [
    url(r'^$', views.index, ),
]
