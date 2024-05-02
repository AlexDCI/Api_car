from django.urls import path
from cars.views import CarApiView, get_weather

urlpatterns = [
    
    path('api/v1/cars/', CarApiView.as_view()),
    path('weather/', get_weather, name='weather'),
    
]
