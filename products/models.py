from django.db import models

# Create your models here.



class Item(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField()
	price=models.FloatField()
	created=models.DateTimeField(auto_now_add=True, auto_now=False)
	updated=models.DateTimeField(auto_now_add=False, auto_now=True)
	slug=models.SlugField()
	active=models.BooleanField(default=True)


	def __unicode__(self):
		return self.title

	def get_price(self):
		return self.price