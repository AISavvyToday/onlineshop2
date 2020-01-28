from django.contrib import admin
from . models import Cart, CartItem

# Register your models here.



class  CartAdmin(admin.ModelAdmin):
	class Meta:
		model = Cart



	"""docstring for  CartAdmin"""
	# def __init__(self, arg):
	# 	super( CartAdmin, self).__init__()
	# 	self.arg = arg


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)



