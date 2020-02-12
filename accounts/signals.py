import random
import hashlib
import stripe
from django.conf import settings

from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from . models import UserStripe, EmailConfirmed


stripe.api_key = settings.STRIPE_SECRET_KEY


# incase i want to create stripe_id when a user logs in instead

# def get_or_create_stripe(sender, user, *args, **Kwargs):

# 	try:
# 		user.userstripe.stripe_id
# 	except UserStripe.DoesNotExist:
# 		customer = stripe.Customer.create(
# 		email = str(user.email)
# 		)
# 		new_user_stripe = UserStripe.objects.create(
# 			user=user,
# 			stripe_id = customer.id
# 			)
# 	except:
# 		pass
# user_logged_in.connect(get_or_create_stripe)		

def get_create_stripe(user):
	try:
		user.userstripe.stripe_id
	except UserStripe.DoesNotExist:
		customer = stripe.Customer.create(

			email = str(user.email)

			)
		new_user_stripe = UserStripe.objects.create(
			user=user,
			stripe_id=customer.id

			)
	except:
		pass


def user_created(sender, instance, created, *args, **Kwargs):
	user = instance

	if created:
		get_create_stripe(user)
		email_confirmed, email_is_created = EmailConfirmed.objects.get_or_create(user=user)
		if email_is_created:
			short_hash = hashlib.sha1(str(random.random()).encode()).hexdigest()[:5]
			base, domain = str(user.email).split('@')
			activation_key = hashlib.sha1((short_hash+base).encode()).hexdigest()
			email_confirmed.activation_key = activation_key
			email_confirmed.save()
			email_confirmed.activate_user_email()
			

post_save.connect(user_created, sender=settings.AUTH_USER_MODEL)
