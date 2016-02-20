from __future__ import unicode_literals
from django.db import models
from login.models import fbUser
# Create your models here.
class Friend(models.Model):
	fbuser = models.ForeignKey(fbUser,on_delete=models.CASCADE)
	friend = models.CharField(max_length=40,null=False,blank=False)
	#friend = models.ManyToManyField(fbUser,related_name="friendOfUser")
	def __unicode__(self):
		return self.friend