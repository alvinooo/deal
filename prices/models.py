import uuid

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Item(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "1. Items"


class Store(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "2. Stores"


class ItemInstance(models.Model):
    name = models.ForeignKey(Item, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    price = models.FloatField()
    quantity = models.FloatField()
    unit = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "3. ItemsInstances"


class CurrentBest(models.Model):
    name = models.ForeignKey(ItemInstance, on_delete=models.CASCADE, related_name='best')
    next_best = models.ForeignKey(ItemInstance, on_delete=models.CASCADE, related_name='next_best', blank=True)
    purchase_date = models.DateField()
    price = models.FloatField()
    quantity = models.FloatField()

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "4. CurrentBests"


class Recipes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    item = models.ForeignKey(ItemInstance, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "5. Recipes"

class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey(Store, on_delete=CASCADE)
    item = models.ForeignKey(ItemInstance, on_delete=CASCADE)

    def __str__(self) -> str:
        return str(self.store)

    class Meta:
        verbose_name_plural = "6. Trips"