from django.db import models
from django.contrib.auth.models import AbstractUser
from crud_api.manager import UserManager
from helpers.models import Dropdown


# Create your models here.
class CustomUser(AbstractUser):
	first_name  = models.CharField(max_length=50 , null=False , blank=False)
	last_name  = models.CharField(max_length=50 , null=False , blank=False)
	email = models.EmailField(verbose_name = 'user_email', null=True, blank=True , unique=True)
	mobile = models.CharField(max_length=12, null=True , blank=True) 
	role = models.ForeignKey(Dropdown , on_delete=models.DO_NOTHING , null=True , blank=True)


	USERNAME_FIELD='email'
	REQUIRED_FIELDS=[]

	objects=UserManager()

	def __str__(self):
		return self.email

class Employee(models.Model):
	user =  models.ForeignKey(CustomUser , on_delete=models.CASCADE , related_name='employee_customUser',null= True,blank=True)
	emp_id    =  models.CharField(auto_created = True,primary_key=True , max_length=6)
	designation= models.ForeignKey(Dropdown , on_delete=models.CASCADE , related_name='employee_dropdown_desig',null= True,blank=True)
	company = models.CharField(max_length=50 , blank=True , null=True)
	created_at = models.DateField(auto_now_add = True)
	updated_at = models.DateField(auto_now = True)






