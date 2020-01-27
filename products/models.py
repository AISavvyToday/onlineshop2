from django.urls import reverse
from django.db import models

# Create your models here.



class Item(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	sale_price = models.FloatField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	slug = models.SlugField(unique=True)
	active = models.BooleanField(default=True)


	def __unicode__(self):
		return self.title


	class meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price


	def get_absolute_url(self):
		return reverse('single_item', kwargs={'slug': self.slug })



class ItemImage(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products/images/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)



	def __unicode__(self):
		return self.item.title