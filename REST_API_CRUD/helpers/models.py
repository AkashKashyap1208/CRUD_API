from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Dropdown(models.Model):
	""" table that stores the values of drop down in the system """

	name = models.CharField(max_length = 255)
	slug = models.CharField(max_length = 255)


	def safe (self,*args , **kwargs):
		if not self.slug:
			pass
		else:
			self.slug = slugify(self.designation_name)
			super().save(*args,**kwargs)

	def __str__(self):
		return self.name


