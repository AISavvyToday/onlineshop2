from django.db import models
from products.models import Item, Variation 

# Create your models here.



class Cart(models.Model):
	total = models.FloatField(default=0.00)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		get_latest_by = "updated"


	def __str__(self):
		return "Cart Id: %s" %(self.id)



class CartItem(models.Model):
	
	cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
	variations = models.ManyToManyField(Variation, null=True, blank=True)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	notes = models.TextField(null=True, blank=True)
	line_total = models.FloatField(default=0.00)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.item.title