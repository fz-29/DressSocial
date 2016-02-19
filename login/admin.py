from django.contrib import admin
from login.models import fbUser
# Register your models here.
class loginAdmin(admin.ModelAdmin):
	list_display = ("fbid","__unicode__","lname")
	class Meta :
		model = fbUser

admin.site.register(fbUser,loginAdmin)