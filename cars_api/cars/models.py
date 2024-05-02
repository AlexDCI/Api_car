from django.db import models

class Car(models.Model):
    model_car = color_car = models.CharField(max_length=50)
    color_car = models.CharField(max_length=50)
    relise_data = models.DateField(null=True)
    prise = models.DecimalField(max_digits=10, decimal_places=2)
    car_type = models.ForeignKey('TypeCar', on_delete=models.CASCADE, null=True)
    description_car = models.TextField(blank=True)


class TypeCar(models.Model):
    type = models.CharField(max_length=100, db_index=True)

    def __str__(self) -> str:
        return self.type
    