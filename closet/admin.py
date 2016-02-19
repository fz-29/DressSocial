from django.contrib import admin

# Register your models here.
from closet.models import Wardrobe, Combination
# Register your models here.
class WardrobeAdmin(admin.ModelAdmin):
	list_display = ("__unicode__","image")
	class Meta :
		model = Wardrobe
class CombinationAdmin(admin.ModelAdmin):
	list_display = ("__unicode__","fbuser")
	class Meta :
		model = Combination

admin.site.register(Wardrobe,WardrobeAdmin)
admin.site.register(Combination,CombinationAdmin)