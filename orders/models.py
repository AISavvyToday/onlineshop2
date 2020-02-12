from django.contrib.auth import get_user_model
from django.db import models
from carts.models import Cart

# Create your models here.

User = get_user_model()
STATUS_CHOICES = (
	("Started", "Started"),
	("Abandoned", "Abandoned"),
	("Finished", "Finished")
)

class Order(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	order_id = models.CharField(max_length=120, default="ABC", unique=True)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	status = models.CharField(max_length=150, choices=STATUS_CHOICES, default='started')
	sub_total = models.FloatField(default=0.00)
	tax_total = models.FloatField(default=0.00)
	final_total = models.FloatField(default=0.00)
	created = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)


	def __str__(self):
		return self.order_id

	def get_final_amount(self):
		instance = Order.objects.get(id=self.id)
		instance.tax_total = 0.16 * self.sub_total
		instance.final_total = self.sub_total + instance.tax_total
		instance.save()
		return instance.final_total