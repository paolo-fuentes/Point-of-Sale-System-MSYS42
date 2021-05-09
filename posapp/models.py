from django.db import models
from datetime import datetime
from django.utils import timezone

now = timezone.now()

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=25, default=None)
    item_price=models.IntegerField(default=None)
    stock_quantity=models.IntegerField(default=None)

    def getPrice(self):
        return self.item_price

    def __str__(self):
        return self.item_name

    def depleteStock(self, value):
        self.stock_quantity -= value
        self.save()

class Order(models.Model):
    total_amount=models.DecimalField(max_digits=10, decimal_places=2)
    order_date=models.DateField(default=timezone.now)
    class ptype(models.IntegerChoices):
        CASH = 1
        CARD = 2
    payment_type=models.IntegerField(choices=ptype.choices)
    objects = models.Manager()

    def getPk(self):
        return self.pk
    
    def __str__(self):
        return str(self.pk) + ": " + str(self.order_date) + " - " + str(self.total_amount)

class ItemOrder(models.Model):
    item_id=models.ForeignKey(Item, on_delete = models.SET_NULL, null=True)
    order_id=models.ForeignKey(Order, on_delete = models.SET_NULL, null=True)
    line_total=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.IntegerField(default=None)
    objects = models.Manager()

    def __str__(self):
        return str(self.item_id)

    