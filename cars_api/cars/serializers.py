from rest_framework import serializers
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('model_car', 'color_car', 'id', 'car_type_id')