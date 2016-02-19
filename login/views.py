from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import fbUser
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
@require_POST
def fblogin(request):	
	response_data={}
	input = request.POST
	#check incase of error 
	try :
		obj = fbUser.objects.get(fbid=input['fbid'])
		response_data['success']='1'
		response_data['new-user']='0'
		return JsonResponse(response_data)

	except fbUser.DoesNotExist:
		name = fbUser.objects.create(fbid=input['fbid'],fname=input['fname'],lname=input['lname'],email=input['email'],gender=input['gender'])
		response_data['success']='1'
		response_data['new-user']='1'
		return JsonResponse(response_data)