from django.conf import settings
from django.db import models
from carts.models import Cart
from accounts.models import UserAddress

# Create your models here.



STATUS_CHOICES = (
	("Started", "Started"),
	("Abandoned", "Abandoned"),
	("Finished", "Finished")
)

try:
	tax_rate = settings.DEFAULT_TAX_RATE
except Exception as e:
	raise NotImplemetedError(str(e))



class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
	order_id = models.CharField(max_length=120, default="ABC", unique=True)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	status = models.CharField(max_length=150, choices=STATUS_CHOICES, default='started')
	shipping_address = models.ForeignKey(UserAddress,null=True,related_name='shipping_address',\
							on_delete=models.CASCADE)
	billing_address = models.ForeignKey(UserAddress,null=True,related_name='billing_address',\
							on_delete=models.CASCADE)
	sub_total = models.FloatField(default=0.00)
	tax_total = models.FloatField(default=0.00)
	final_total = models.FloatField(default=0.00)
	created = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)


	def __str__(self):
		return self.order_id

	def get_final_amount(self):
		instance = Order.objects.get(id=self.id)
		instance.tax_total = tax_rate * self.sub_total
		instance.final_total = self.sub_total + instance.tax_total
		instance.save()
		return instance.final_total