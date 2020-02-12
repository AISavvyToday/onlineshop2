from django.contrib import admin
from . models import Item, ItemImage, Variation, Category

# Register your models here.



class ItemAdmin(admin.ModelAdmin):
	date_hierarchy= 'created' # or updated
	search_fields = ['title', 'description']
	list_display=['title', 'price', 'active', 'updated']
	list_editable=['price', 'active']
	list_filter=['price', 'active']
	readonly_fields = ['created', 'updated']
	prepopulated_fields = {'slug':('title',)}
	class Meta:
		model = Item


admin.site.register(Item, ItemAdmin )
admin.site.register(ItemImage)
admin.site.register(Variation)
admin.site.register(Category)