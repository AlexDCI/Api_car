from rest_framework import serializers
from cars.models import Car, TypeCar
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io



class CarSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Car
        fields = ('__all__')





    # model_car = serializers.CharField(max_length=50)
    # color_car = serializers.CharField(max_length=50)
    # relise_data = serializers.DateField()
    # price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # car_type = serializers.PrimaryKeyRelatedField(queryset=TypeCar.objects.all())
    # description_car = serializers.CharField(allow_blank=True)

    # def create(self, validated_data):
    #     return Car.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.model_car = validated_data.get("model_car", instance.model_car)
    #     instance.color_car = validated_data.get("color_car", instance.color_car)
    #     instance.relise_data = validated_data.get("relise_data", instance.relise_data)
    #     instance.price = validated_data.get("price", instance.price)
    #     instance.car_type = validated_data.get("car_type", instance.car_type)
    #     instance.description_car = validated_data.get("description_car", instance.description_car)
    #     instance.save()
    #     return instance

    
# def encode():
#     obj_model = CarModel('Alfa Romeo', 'It is Italyeno car for every day driving')
#     obj_sr = CarSerializer(obj_model)
#     print(obj_sr.data, sep='\n')
#     json = JSONRenderer().render(obj_sr.data)
#     print(json)


# def decode():
#     stream = io.BytesIO(b'{"model_name":"Alfa Romeo","description":"It is Italyeno car for every day driving"}')
#     data = JSONParser().parse(stream)
#     serializer = CarSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)







# OLD TASKS

# from rest_framework import serializers
# from cars.models import Car
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# import io


# class CarModel:
#     def __init__(self, model_car, color_car):
#         self.model_car = model_car
#         self.color_car = color_car


# class CarSerializer(serializers.Serializer):
#     model_car = color_car = serializers.CharField(max_length=50)
#     color_car = serializers.CharField(max_length=50)
#     relise_data = serializers.DateField()
#     prise = serializers.DecimalField(max_digits=10, decimal_places=2)
#     car_type = serializers.CharField()
#     description_car = serializers.CharField()



# def endcode():
#     model = CarModel('Lamborgini', 'Red')
#     model_sr = CarSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n') 
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"model_car":"Lamborgini", "color_car":"Red"}')
#     data = JSONParser().parse(stream)
#     serializer = CarSerializer(data=data)
#     serializer.is_valid()
#     print(serializer._validated_data)
    