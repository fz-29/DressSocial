from django.shortcuts import render
from .models import Wardrobe, Combination
from login.models import fbUser
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.http import HttpResponse,JsonResponse
from django.core import serializers
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
		response_data["tops"] = tops
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
		response_data["bottoms"] = tops
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def giveFoot(request):
	response_data={}
	fbid = request.POST["fbid"]
	try :
		fbObj = fbUser.objects.get(fbid = fbid)
		topObjs = Wardrobe.objects.filter(fbuser = fbObj, dressType = 'foot')
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
	acc = request.POST["accid"]
	access = request.POST["access"]

	try :
		fbObj = fbUser.objects.get(fbid=fbid)
		# topObj = Wardrobe.objects.get(id=topid)
		# bottomObj = Wardrobe.objects.get(id=bottomid)
		# footObj = Wardrobe.objects.get(id=footid)
		# accObj = Wardrobe.objects.get(id=accid)
		Combination.objects.create(fbuser=fbObj, combinationName=combinationName ,trend= trend , topLink = top,bottomLink = bottom ,footLink = foot,accLink= acc, access = access)
	except:
		response_data["success"] = "0"
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
			combs += [{ 'name' : itero.combinationName , 'top' : itero.topLink ,'bottom' : itero.bottomLink, "foot" : itero.footLink, "acc" : itero.accLink }]
		response_data["acc"] = combs
		return JsonResponse(response_data)