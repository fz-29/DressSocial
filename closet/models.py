from django.db import models
from login.models import fbUser
# Create your models here.
class Wardrobe(models.Model):
	fbuser = models.ForeignKey(fbUser,on_delete=models.CASCADE)
	dressName = models.CharField(max_length=50,null=True)
	dressType = models.CharField(max_length=40,null=True)
	image = models.CharField(max_length=3000,null=False,blank=False,unique=True,primary_key=True)
	url = models.CharField(max_length=3000,null=True,blank=True,unique=True)
	color = models.CharField(max_length=40,null=True)
	access = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.dressName

class Combination(models.Model):
	fbuser = models.ForeignKey(fbUser,on_delete=models.CASCADE)
	combinationName = models.CharField(max_length=50,null=True)
	trend = models.CharField(max_length=2000,null=True)
	topLink = models.CharField(max_length=2000,null=True)
	bottomLink = models.CharField(max_length=2000,null=True)
	footLink = models.CharField(max_length=2000,null=True)
	accLink = models.CharField(max_length=2000,null=True)
	access = models.IntegerField(default=0)
	date = models.DateField(null=True)
	def __unicode__(self):
		return self.combinationName