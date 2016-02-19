from django.shortcuts import render
from .models import Wardrobe, Combination
from login.models import fbUser
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.http import HttpResponse,JsonResponse
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

# def provide(request):

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
		Combination.objects.create(fbuser=fbObj ,combinationName=combinationName ,trend= trend , topLink = top,bottomLink = bottom ,footLink = foot,accLink= acc, access = access)
	except:
		response_data["success"] = "0"
		return JsonResponse(response_data)
	else:
		response_data["success"] = "1"
		return JsonResponse(response_data)