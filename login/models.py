from django.db import models
# Create your models here.
class fbUser(models.Model):
	fbid=models.CharField(max_length=40,null=False,blank=False,unique=True,primary_key=True)
	fname=models.CharField(max_length=20,null=False,blank=False)
	lname=models.CharField(max_length=15,null=False,blank=False)
	email=models.EmailField(null=True,blank=True)
	gender=models.CharField(max_length=10,null=False,blank=False)
	
	def __unicode__(self):
		return self.fname
