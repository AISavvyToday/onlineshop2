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


	def __str__(self):
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



	def __str__(self):
		return self.item.title


class VariationManager(models.Manager):

	def all(self):
		return super(VariationManager,self).filter(active=True)

	def sizes(self):
		return self.all().filter(category='size')

	def colors(self):
		return self.all().filter(category='color')

	def packages(self):
		return self.all().filter(category='package')

VAR_CATEGORIES = (
	('size','size'),
	('color', 'color'),
	('package', 'package'),
)

class Variation(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
	image = models.ForeignKey(ItemImage, null=True, blank=True, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	objects = VariationManager()
	

	def __str__(self):
		return self.title