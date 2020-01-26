from django.db import models

# Create your models here.



class Item(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True)
	price = models.FloatField()
	sale_price = models.FloatField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	slug = models.SlugField()
	active = models.BooleanField(default=True)


	def __unicode__(self):
		return self.title

	def get_price(self):
		return self.price




class ItemImage(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products/images/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)



	def __unicode__(self):
		return self.item.title