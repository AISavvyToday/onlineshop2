from django.db import models
from products.models import Item

# Create your models here.



class Cart(models.Model):
	items = models.ManyToManyField(Item, null=True, blank=True)
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)


	def __unicode__(self):
		return "Card Id: %s" %(self.id)