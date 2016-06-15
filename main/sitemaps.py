#!/usr/bin/env python
from django.contrib.sitemaps import Sitemap
from .models import Instance

class InstanceSitemap(Sitemap):

	changefreq = 'weekly'
	priority = 0.9
   
	def items(self):
		return Instance.objects.all()

	def lastmod(self, obj):
		return obj.updated_date