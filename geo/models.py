from django.db import models

# Create your models here.

class GeoObject(models.Model):
	geo1_lat = models.FloatField('lat1', null=True, blank=True)
	geo1_lon = models.FloatField('lon1', null=True, blank=True)
	geo2_lat = models.FloatField('lat2', null=True, blank=True)
	geo2_lon = models.FloatField('lon2', null=True, blank=True)
	geo3_lat = models.FloatField('lat3', null=True, blank=True)
	geo3_lon = models.FloatField('lon3', null=True, blank=True)
	geo4_lat = models.FloatField('lat4', null=True, blank=True)
	geo4_lon = models.FloatField('lon4', null=True, blank=True)

	def __unicode__(self):
		return str(self.geo1_lat) + " " + str(self.geo2_lat) + " " + str(self.geo3_lat) + " " + str(self.geo4_lat)