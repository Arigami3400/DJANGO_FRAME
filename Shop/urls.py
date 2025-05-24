from django.urls import path
from .views import InformationViewSet


urlparrens = [
    path('',InformationViewSet.as_view({'get':'list'}), name = 'Information_list')
]