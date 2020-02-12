
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.db import models
from django.template.loader import render_to_string



# Create your models here.
class USerDefaultAddress(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	shipping = models.ForeignKey('UserAddress', blank=True, null=True,\
					related_name='user_address_shipping_default', on_delete=models.CASCADE)
	billing = models.ForeignKey('UserAddress', blank=True, null=True,\
					related_name='user_address_billing_default', on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user.username)





class UserAddressManager(models.Manager):
	def get_billing_addresses(self, user):
		return super(UserAddressManager, self).filter(billing=True).filter(user=user)


class UserAddress(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	address = models.CharField(max_length=200)
	address2 = models.CharField(max_length=200, null=True, blank=True)
	country = models.CharField(max_length=120)
	zip_code = models.CharField(max_length=25)
	county = models.CharField(max_length=120, null=True, blank=True)
	town = models.CharField(max_length=120)
	phone = models.CharField(max_length=120)
	shipping = models.BooleanField(default=True)
	billing = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.get_address()

	def get_address(self):
		return '%s, %s, %s, %s, %s' %(self.address, self.country, self.zip_code, self.county, self.town)

	objects = UserAddressManager()

	class Meta:
		ordering = ['updated','-created']



class UserStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	stripe_id = models.CharField(max_length=120, null=True, blank=True)


	def __str__(self):
		return str(self.stripe_id)


class EmailConfirmed(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	activation_key = models.CharField(max_length=200)
	confirmed = models.BooleanField(default=False)
	def __str__(self):
		return str(self.confirmed)
	def activate_user_email(self):
		activation_url = '%s%s' %(settings.SITE_URL, reverse('activate', args=[self.activation_key]))
		context = {
			'activation_key': self.activation_key,
			'activation_url': activation_url,
			'user': self.user.username
		}
		message = render_to_string('activation_message.txt', context)
		subject = 'Activate your email'
		self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.user.email], kwargs)


class EmailMarketingSignUp(models.Model):
	email = models.EmailField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	# confirmed = models.BooleanField(default=False)

	def __str__(self):
		return str(self.email)




