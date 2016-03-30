from django.conf.urls import include, url,static
urlpatterns=[
	url(r'^add/$','friend.views.addFriends',name='add'),
	url(r'^get/$','friend.views.getFriends',name='get'),
]