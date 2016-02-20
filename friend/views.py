from django.shortcuts import render
from login.models import fbUser
from .models import Friend
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.http import HttpResponse,JsonResponse
import json
@csrf_exempt
@require_POST
def addFriends(request):
	response_data={}
	fbid = request.POST["fbid"]
	friends = json.loads(request.POST["friends"])
	try :
		personobj = fbUser.objects.get(fbid = fbid)
		for itero in friends :
			frnd = itero["id"]
			friendobj = fbUser.objects.get(fbid = frnd)
			Friend.objects.create(fbuser = personobj, friend = friendobj)
	except Exception as e:		
		response_data["success"]="0"
		return JsonResponse(response_data)
	else:
		response_data["success"]="1"
		return JsonResponse(response_data)
