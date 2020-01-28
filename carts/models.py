from django.db import models
from products.models import Item

# Create your models here.

class CartItem(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.item.title


class Cart(models.Model):
	ordered_items = models.ManyToManyField(CartItem, null=True, blank=True)
	items = models.ManyToManyField(Item, null=True, blank=True)
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		get_latest_by = "updated"


	def __str__(self):
		return "Card Id: %s" %(self.id)