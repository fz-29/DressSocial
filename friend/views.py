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
		objInfbUser = fbUser.objects.get(fbid=fbid)
		objInFriend = Friend.objects.filter(fbuser = objInfbUser)
		if len(objInFriend) == 0:
			#user does not have any friends yet
			objInFriend = Friend(fbuser = objInfbUser)
			objInFriend.save()
		else:
			objInFriend = objInFriend[0]
		for itero in friends :
			person = fbUser.objects.get(fbid = itero["id"])
			objInFriend.friend.add(person)
	except Exception as e:		
		response_data["success"]="0"
		return JsonResponse(response_data)
	else:
		response_data["success"]="1"
		return JsonResponse(response_data)
@csrf_exempt
@require_POST
def getFriends(request):
	response_data={}
	fbid = request.POST["fbid"]
	friend_array = []
	try :
		personobj = fbUser.objects.get(fbid = fbid)
		objInFriend = Friend.objects.filter(fbuser = personobj)[0]
		friends = objInFriend.friend.all()
		for friend in friends :
			dic = {"id" : friend.fbid ,"name" : friend.fname}
			friend_array.append(dic)
	except Exception as e:
		response_data["success"]="0"
		return JsonResponse(response_data)
	else:
		response_data["success"]="1"
		response_data["friends"] = friend_array
		return JsonResponse(response_data)