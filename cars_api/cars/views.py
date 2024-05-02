from django.shortcuts import render
from rest_framework import generics
from cars.models import Car
from cars.serializers import CarSerializer
from rest_framework.views import APIView

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps



class CarApiView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



def get_weather(request):
    owm = OWM('ca691c0a077b7441f179a898670138e2')
    mgr = owm.weather_manager()

    # Search for current weather in Rostok, Germany and get details
    observation = mgr.weather_at_place('Rostok,DE')
    weather = observation.weather

    context = {
        'detailed_status': weather.detailed_status,
        'wind_speed': weather.wind().get('speed'),
        'humidity': weather.humidity,
        'temperature': weather.temperature('celsius').get('temp'),
        'clouds': weather.clouds
    }

    return render(request, 'cars/weather.html', context)

