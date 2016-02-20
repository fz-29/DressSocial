from django.contrib import admin
from friend.models import Friend
# Register your models here.
class FriendAdmin(admin.ModelAdmin):
	list_display = ("fbuser","__unicode__")
	class Meta :
		model = Friend

admin.site.register(Friend,FriendAdmin)