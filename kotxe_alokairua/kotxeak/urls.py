from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('cars', views.cars, name='cars'),
    path('autoak_gehitu', views.autoak_gehitu, name='autoak_gehitu'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/', views.updaterecord, name='updaterecord'),
]