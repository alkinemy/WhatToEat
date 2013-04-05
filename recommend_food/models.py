from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Categories(models.Model):
	Name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.Name
	
class Regions(models.Model):
	Name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.Name

class Restaurants(models.Model):
	Name = models.CharField(max_length=200)
	Category = models.ForeignKey(Categories)
	PhoneNumber = models.CharField(max_length=200)
	Region = models.ForeignKey(Regions)
	
	def __unicode__(self):
		return self.Name
	
class Foods(models.Model):
	Name = models.CharField(max_length=200)
	Price = models.IntegerField()
	Restaurant = models.ForeignKey(Restaurants)

	def __unicode__(self):
		return self.Name
