from django.shortcuts import render
from .models import Wardrobe, Combination
from login.models import fbUser
from friend.models import Friend
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.http import HttpResponse,JsonResponse
import datetime

# Create your views here.
@csrf_exempt
@require_POST
def update(request):
	fbid = request.POST["fbid"]
	dressName = request.POST["dressName"]
	dressType = request.POST["dressType"]
	image = request.POST["image"]
	color = request.POST["color"]
	access = request.POST["access"]
	response_data={}

	try :
		obj = fbUser.objects.get(fbid=fbid)
		Wardrobe.objects.create(fbuser = obj,dressName=dressName, dressType=dressType,image=image, color= color, access= access)	
	except:
		response_data["success"]="0"
		return JsonResponse(response_data)
	else:
		response_data["success"]="1"
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def giveTop(request):
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
		#jsonObj = serializers.serialize("json", topObjs)
		tops = []
		for itero in topObjs:
			tops += [{ 'name' : itero.dressName, 'image' : itero.image }]
		response_data["top"] = tops
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def giveBottom(request):
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
			tops += [{ 'name' : itero.dressName, 'image' : itero.image }]
		response_data["bottom"] = tops
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def giveFoot(request):
	response_data={}
	fbid = request.POST["fbid"]
	try :
		fbObj = fbUser.objects.get(fbid = fbid)
		topObjs = Wardrobe.objects.filter(fbuser = fbObj, dressType = 'footwear')
	except:
		response_data["success"] = "0"
		return JsonResponse(response_data)
	else:
		response_data["success"] = "1"
		
		tops = []
		for itero in topObjs:
			tops += [{ 'name' : itero.dressName, 'image' : itero.image }]
		response_data["foot"] = tops
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def giveAcc(request):
	response_data={}
	fbid = request.POST["fbid"]
	try :
		fbObj = fbUser.objects.get(fbid = fbid)
		topObjs = Wardrobe.objects.filter(fbuser = fbObj, dressType = 'acc')
	except:
		response_data["success"] = "0"
		return JsonResponse(response_data)
	else:
		response_data["success"] = "1"
		
		tops = []
		for itero in topObjs:
			tops += [{ 'name' : itero.dressName, 'image' : itero.image }]
		response_data["acc"] = tops
		return JsonResponse(response_data)

def getShade(request):	
	from colorthief import ColorThief
	color_thief = ColorThief('images.jpg')
	dominant_color = color_thief.get_color(quality=1)
	palette=color_thief.get_palette(color_count=6)

	comp_color={'green':'magenta','white':'black','blue':'red','red':'blue','black':'white'}

	img1=cv2.imread(request.POST["image"],0)
	ref=ColorThief(request.POST["image"])#ref image is the image being checked
	dominant_color=ref.get_color(quality=1)
	#print img1.shape
	refR,refG,refB=dominant_color
	#print refR,refG,refB
	compR=255-refR
	compG=255-refG
	compB=255-refB
	return dominant_color;

@csrf_exempt
@require_POST
def addCombination(request):
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
	response_data = {}
	fbid = request.POST["fbid"]
	try :
		fbObj = fbUser.objects.get(fbid=fbid)
		combinationsObj = Combination.objects.filter(fbuser=fbObj)
	except:
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
	response_data = {}
	fbid = request.POST["fbid"]
	try :
		fbObj = fbUser.objects.get(fbid=fbid)
		friendObj = Friend.objects.filter(fbuser=fbObj)
		combinationsObj = [];
		for itero in friendObj : 
			friendComb = Combination.objects.filter(fbuser=itero, date = datetime.date.today())
			dictn = {"name" : friendComb.fbuser , "top" : friendComb.topLink ,"foot" : friendComb.bottomLink ,"bottom" : friendComb.footLink }
			combinationsObj.append(friendComb)
			
	except:
		response_data["success"] = "0"
		return JsonResponse(response_data)
	else:
		response_data["success"] = "1"
		response_data["data"] = combinationsObj
		return JsonResponse(response_data)