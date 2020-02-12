from django.urls import reverse
from django.db import models
from django.db.models.signals import post_save  

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	slug = models.SlugField(unique=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	featured = models.BooleanField(default=None)
	active = models.BooleanField(default=True)


	def __str__(self):
		return self.title


	
class Item(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	category = models.ManyToManyField(Category,null=True, blank=True)
	price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	sale_price = models.FloatField(null=True, blank=True)
	slug = models.SlugField(unique=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	update_defaults = models.BooleanField(default=False)


	def __str__(self):
		return self.title


	class meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price


	def get_absolute_url(self):
		return reverse('single-item', kwargs={'slug': self.slug })



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



# T-shirt 5
# Active Wear 6

def item_defaults(sender, instance, created, *args, **kwargs):
	if instance.update_defaults:
		categories = instance.category.all()
		print(categories)
		for cat in categories: 
			print(cat.id)
			if cat.id == 5:#id for tshirt #----> create function for handling all category ids
				small_size = Variation.objects.get_or_create(item=instance,category='size',title='Small')
				medium_size = Variation.objects.get_or_create(item=instance,category='size',title='Medium')
				large_size = Variation.objects.get_or_create(item=instance,category='size',title='Large')


		instance.update_defaults = False
		instance.save()


post_save.connect(item_defaults, sender=Item)