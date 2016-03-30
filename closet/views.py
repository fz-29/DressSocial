import cloudinary
import cloudinary.uploader
import cloudinary.api
import colorsys
from django.shortcuts import render
from .models import Wardrobe, Combination
from login.models import fbUser
from friend.models import Friend
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.http import HttpResponse,JsonResponse
import datetime

def getComplementary(image):
	'''Find the shade of the clothes'''	
	dom_color = cloudinary.api.resource(image, colors = True)['colors'][0][0]
	comp_color={'green':'magenta','white':'black','blue':'red','red':'blue','black':'white'}
	return (dom_color,"black")

# Create your views here.
@csrf_exempt
@require_POST
def update(request):
	'''To add new clothes'''
	fbid = request.POST["fbid"]
	dressName = request.POST["dressName"]
	dressType = request.POST["dressType"]
	image = request.POST["image"]
	url = request.POST["url"]
	access = request.POST["access"]
	#color,comp_color = getComplementary(image)
	color = "black"
	comp_color = "black"
	response_data={}
	try :
		obj = fbUser.objects.get(fbid=fbid)
		Wardrobe.objects.create(fbuser = obj,dressName=dressName, dressType=dressType,image=image, url = url, color= color, access= access)	
	except:
		response_data["success"]="0"
		return JsonResponse(response_data)
	else:
		response_data["success"]="1"
		response_data["comp_color"]=comp_color
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def giveTop(request):
	'''Fetch top'''
	response_data={}
	fbid = request.POST["fbid"]
	try :
		fbObj = fbUser.objects.get(fbid = fbid)
		topObjs = Wardrobe.objects.filter(fbuser = fbObj, dressType = 'top')
	except:
		response_data["success"] = "0"
		return JsonResponse(response_data)
	else:
		response_data["success"] = "1"
		tops = []
		for itero in topObjs:
			tops += [{ 'name' : itero.dressName, 'image' : itero.image, 'url' : itero.url }]
		response_data["top"] = tops
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def giveBottom(request):
	'''Fetch bottom'''
	response_data={}
	fbid = request.POST["fbid"]
	try :
		fbObj = fbUser.objects.get(fbid = fbid)
		topObjs = Wardrobe.objects.filter(fbuser = fbObj, dressType = 'bottom')
	except:
		response_data["success"] = "0"
		return JsonResponse(response_data)
	else:
		response_data["success"] = "1"
		
		tops = []
		for itero in topObjs:
			tops += [{ 'name' : itero.dressName, 'image' : itero.image, 'url' : itero.url }]
		response_data["bottom"] = tops
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def giveFoot(request):
	'''Fetch Footwear'''
	response_data={}
	fbid = request.POST["fbid"]
	try :
		fbObj = fbUser.objects.get(fbid = fbid)
		topObjs = Wardrobe.objects.filter(fbuser = fbObj, dressType = 'footwear')
	except:
		print 
		response_data["success"] = "0"
		return JsonResponse(response_data)
	else:
		response_data["success"] = "1"
		
		tops = []
		for itero in topObjs:
			tops += [{ 'name' : itero.dressName, 'image' : itero.image, 'url' : itero.url }]
		response_data["foot"] = tops
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def giveAcc(request):
	'''Fetch access'''
	response_data={}
	fbid = request.POST["fbid"]
	try:

		fbObj = fbUser.objects.get(fbid = fbid)
		topObjs = Wardrobe.objects.filter(fbuser = fbObj, dressType = 'acc')
	except:
		response_data["success"] = "0"
		return JsonResponse(response_data)
	else:
		response_data["success"] = "1"
		
		tops = []
		for itero in topObjs:
			tops += [{ 'name' : itero.dressName, 'image' : itero.image, 'url' : itero.url }]
		response_data["acc"] = tops
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def addCombination(request):
	'''Add the combination into the databse from  DRESS SELECTOR activity '''
	response_data = {}
	fbid = request.POST["fbid"]
	combinationName = request.POST["dressName"]
	trend = request.POST["trend"]
	top = request.POST["topid"]
	bottom = request.POST["bottomid"]
	foot = request.POST["footid"]
	# acc = request.POST["accid"]
	access = int(request.POST["access"])
	try :
		fbObj = fbUser.objects.get(fbid=fbid)
		# topObj = Wardrobe.objects.get(id=topid)
		# bottomObj = Wardrobe.objects.get(id=bottomid)
		# footObj = Wardrobe.objects.get(id=footid)
		# accObj = Wardrobe.objects.get(id=accid)
		Combination.objects.create(fbuser=fbObj, combinationName=combinationName ,trend= trend , topLink = top,bottomLink = bottom ,footLink = foot, access = access)
	except:
		response_data["success"] = "0"
		return JsonResponse(response_data)
	else:
		response_data["success"] = "1"
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def wearToday(request):
	'''Update what user is wearing today'''
	response_data = {}
	fbid = request.POST["fbid"]
	combinationId = request.POST["combinationid"]
	try :
		fbObj = fbUser.objects.get(fbid=fbid)
		# topObj = Wardrobe.objects.get(id=topid)
		# bottomObj = Wardrobe.objects.get(id=bottomid)
		# footObj = Wardrobe.objects.get(id=footid)
		# accObj = Wardrobe.objects.get(id=accid)
		Combination.objects.filter(fbuser= fbObj, id = int(combinationId)).update(date = datetime.date.today())
	except Exception as e:		
		response_data["success"]="0"
		response_data["error"]=e
		return JsonResponse(response_data)
	else:
		response_data["success"] = "1"
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def getCombination(request):
	'''Fetch all the combinations'''
	response_data = {}
	fbid = request.POST["fbid"]
	try : 
		fbObj = fbUser.objects.get(fbid=fbid)		
		combinationsObj = Combination.objects.filter(fbuser=fbObj)
	except Exception as e:
		response_data["success"] = "0"
		return JsonResponse(response_data)
	else:
		response_data["success"] = "1"
		combs = []
		for itero in combinationsObj:
			combs += [{ 'id': itero.id ,'name' : itero.combinationName , 'top' : itero.topLink ,'bottom' : itero.bottomLink , 'foot' : itero.footLink }]
		response_data["data"] = combs
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def getFriendCombination(request):
	''' Get friends combinations '''
	pass


	# try :
	# 	fbObj = fbUser.objects.get(fbid=fr)
	# 	friendObj = Friend.objects.filter(fbuser=fbObj)
	# 	combinationsObj = [];
	# 	for itero in friendObj : 
	# 		friendComb = Combination.objects.filter(fbuser=itero, date = datetime.date.today())
	# 		dictn = {"name" : friendComb.fbuser , "top" : friendComb.topLink ,"foot" : friendComb.bottomLink ,"bottom" : friendComb.footLink }
	# 		combinationsObj.append(friendComb)
			
	# except:
	# 	response_data["success"] = "0"
	# 	return JsonResponse(response_data)
	# else:
	# 	response_data["success"] = "1"
	# 	response_data["data"] = combinationsObj
	# 	return JsonResponse(response_data)