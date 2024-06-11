from django.shortcuts import render
from rest_framework. response import Response
from rest_framework.views import APIView
from cars.models import Car, TypeCar
from django.forms import model_to_dict
from cars.serializers import CarSerializer
from rest_framework import status, generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from cars.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly



class CarAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )



class CarAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated, )


class CarAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly, )

    


# class CarViewSet(viewsets.ModelViewSet):
#     # queryset = Car.objects.all()
#     serializer_class = CarSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:           
#             return Car.objects.all()[:3]
#         return Car.objects.filter(pk=pk)
    
    

#     @action(methods=['get'], detail=True)
#     def carstype(self, request, pk=None):
#         typs = TypeCar.objects.get(pk=pk)
#         return Response({'typs': typs.type})


# class CarAPIList(generics.ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer



# class CarAPIUpdate(generics.UpdateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


# class CarAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

    
# class CarApiview(APIView):
#     def get(self, request):
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response({'cars_posts': serializer.data})

#     def post(self, request):
#         serializer = CarSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Car.objects.get(pk=pk)
#         except:
#             return Response({"error": "object does not exists"})
        
#         serializer = CarSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"}, status=status.HTTP_204_NO_CONTENT)
#         try:
#             instance = Car.objects.get(pk=pk)
#             instance.delete()
#             print('instance was deleted sacssefuly', status=status.HTTP_204_NO_CONTENT)
#         except:
#             return Response({"error": "object does not exists"}, status=status.HTTP_204_NO_CONTENT)
        
      
# # OLD TASK
# from rest_framework import generics
# from cars.models import Car
# from cars.serializers import CarSerializer
# from rest_framework.views import APIView
# from rest_framework.views import Response
# from django.forms import model_to_dict
# from rest_framework.response import Response
# from rest_framework import status


# from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps



# def convertor(request):
#     return render(request, 'cars/convertor.html')


# class CarApiView(APIView):
#     def get(self, request):
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response({'cars': serializer.data})
    
#     def post(self, request):
#         serializer = CarSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class CarApiView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer



# def get_weather(request):
#     owm = OWM('ca691c0a077b7441f179a898670138e2')
#     mgr = owm.weather_manager()

#     # Search for current weather in Rostok, Germany and get details
#     observation = mgr.weather_at_place('Rostok,DE')
#     weather = observation.weather

#     context = {
#         'detailed_status': weather.detailed_status,
#         'wind_speed': weather.wind().get('speed'),
#         'humidity': weather.humidity,
#         'temperature': weather.temperature('celsius').get('temp'),
#         'clouds': weather.clouds
#     }

#     return render(request, 'cars/weather.html', context)



# DCI COURSE
