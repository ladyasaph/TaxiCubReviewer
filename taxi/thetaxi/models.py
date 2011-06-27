from django.db import models
from django.contrib import admin
# Create your models here.
class Taxi(models.Model):
	carnumber = models.CharField(max_length = 10, unique = True)
	created = models.DateField(auto_now_add = True)
	def __unicode__(self):
		return self.carnumber

class Ratings(models.Model):
 	RATING_CHOICES = (
        	(1, 'very poor'),
        	(2, 'poor'),
		(3, 'good'),
		(4, 'very good'),
		(5, 'excellent'),
    	)
	rate = models.IntegerField(max_length=10, choices=RATING_CHOICES)
	comment = models.TextField(blank = True)
	author = models.CharField(max_length=15)
	created = models.DateField(auto_now_add = True)
	carnumber  = models.ForeignKey(Taxi)
	def __unicode__(self):
		return self.author

admin.site.register(Taxi)
admin.site.register(Ratings)
