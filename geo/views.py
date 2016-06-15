from django.http import HttpResponse
from .models import GeoObject
from django.core.mail import send_mail
from django.conf import settings
from shapely.geometry import Polygon, Point
# Create your views here.
def mal_track(request):
	args = {}
	status = ''
	lat = request.GET.get('lat', '')
	lon = request.GET.get('lon', '')
	# send_mail('iBox.kg Order' ,"Здравствуйте  Поступил kordinaty ot iBox Mall track:" + " lan is " + str(lat)+ " lon is "+ str(lon) , settings.EMAIL_HOST_USER, ['muratbekov93@gmail.com'], fail_silently=True)
	geo = GeoObject.objects.all()[0]
	poly = Polygon(((geo.geo1_lat, geo.geo1_lon), (geo.geo2_lat, geo.geo2_lon), (geo.geo3_lat, geo.geo3_lon), (geo.geo4_lat, geo.geo4_lon)))
	point = Point(float(lat), float(lon))
	if poly.contains(point):
		status = '<h1>All right biches</h1>'
	else:
		return HttpResponse(status=262)

	return HttpResponse(status)