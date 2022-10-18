from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.pertsonak_index, name='pertsonak_index'),
    path('add_person/', views.pertsonak_gehitu, name='pertsonak_gehitu'),
    path('add_person/addrecord', views.addrecord, name='addrecord'),
    path('addrecord/', views.addrecord, name='addrecord'),


]