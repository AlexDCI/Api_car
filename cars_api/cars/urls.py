from django.urls import path, include, re_path
from cars.views import * # CarViewSet  #CarAPIList, CarAPIDetailView, CarAPIUpdate, get_weather
from rest_framework import routers


# router = routers.SimpleRouter()
# router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [


    # path('api/v1/', include('cars.urls')),

    # path('api/v1/cars/', CarViewSet.as_view({'get': 'list'}), name='cars_list'),
    # path('api/v1/cars/<int:pk>/', CarViewSet.as_view({'put': 'update'}), name='cars_update' ),
    path('api/v1/drf-auth/', include('rest_framework.urls') ),
    path('api/v1/cars/', CarAPIList.as_view(), name='cars_detail_delete' ),
    path('api/v1/cars/<int:pk>/', CarAPIUpdate.as_view(), name='cars_detail_update' ),
    path('api/v1/carsdelete/<int:pk>/', CarAPIDestroy.as_view(), name='cars_detail_delete' ),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/v1/carsdetail/<int:pk>/', CarAPIDetailView.as_view(), name='cars_detail_view' ),
    #path('weather/', get_weather, name='weather'),
  ]  

