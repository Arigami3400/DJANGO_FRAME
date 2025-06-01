from django.urls import path
from .views import InformationViewSet, ProductViewSet

urlparrens = [
    path('',InformationViewSet.as_view({'get':'list','post': 'create'}),
         name = 'Information_list'),
    path('<int:pk>', InformationViewSet.as_view({'get': 'retriv', 'put': 'update',
                                                 'delete': 'destroy'})),
    path('Product', ProductViewSet.as_view({'get':'list','post': 'create'}),
         name = 'Product_list'),
path('Product<int:pk>', ProductViewSet.as_view({'get': 'retriv', 'put': 'update',
                                                'delete': 'destroy'})),

]