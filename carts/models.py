from django.db import models
from products.models import Item

# Create your models here.

class CartItem(models.Model):
	# cart foreign key
	cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	#line total
	line_total = models.DecimalField(default=0.00,max_digits=1000, decimal_places=2)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.item.title


class Cart(models.Model):
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		get_latest_by = "updated"


	def __str__(self):
		return "Card Id: %s" %(self.id)