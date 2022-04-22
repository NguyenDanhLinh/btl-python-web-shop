from django.db import models

from Cart.models import CartItem
from Product.models import Product
from User.models import User


class Order(models.Model):
    customer_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ship_address = models.TextField(null=True, blank=True)
    total = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    total = models.IntegerField(default='0')
    phone = models.TextField(null=True, blank=True)


    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
