from django.conf.urls import include, url,static
urlpatterns=[
	url(r'^$','login.views.fblogin',name='fblogin'),
]
