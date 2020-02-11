from django.contrib import admin
from . models import UserStripe, EmailConfirmed, EmailMarketingSignUp, UserAddress, USerDefaultAddress

# Register your models here.

class UserAddressAdmin(admin.ModelAdmin):

	class Meta:
		model = UserAddress



admin.site.register(UserStripe)
admin.site.register(USerDefaultAddress)
admin.site.register(EmailConfirmed)
admin.site.register(UserAddress, UserAddressAdmin)


class EmailMarketingSignUpAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'created']
	class Meta:
		model = EmailMarketingSignUp



admin.site.register(EmailMarketingSignUp, EmailMarketingSignUpAdmin)
