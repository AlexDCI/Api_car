from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    model_car = color_car = models.CharField(max_length=50)
    color_car = models.CharField(max_length=50)
    relise_data = models.DateField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_type = models.ForeignKey('TypeCar', on_delete=models.CASCADE, null=True)
    description_car = models.TextField(blank=True)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)


class TypeCar(models.Model):
    type = models.CharField(max_length=100, db_index=True)

    def __str__(self) -> str:
        return self.type
    