from django.contrib import admin

# Register your models here.
from closet.models import Wardrobe
# Register your models here.
class WardrobeAdmin(admin.ModelAdmin):
	list_display = ("__unicode__","image")
	class Meta :
		model = Wardrobe

admin.site.register(Wardrobe,WardrobeAdmin)