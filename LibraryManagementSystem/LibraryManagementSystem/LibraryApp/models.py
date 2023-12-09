from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime,timedelta
from django.utils import timezone
from django.conf import settings

# Create your models here.

class User(AbstractUser):
	c=[
	   ('0','Guest'),
	   ('1','Student'),
	   ('2','Librarian'),
	]
	role_type = models.CharField(max_length=5,choices=c,default='0')
	sid = models.CharField(max_length=15)
	has_stregister = models.BooleanField(default=False)
	has_adregister = models.BooleanField(default=False)	

class Profile(models.Model):
	sg = [
		("h","Select Your Gender"),
		('M',"Male"),
		("F","Female")
	]
	usd = models.OneToOneField(User,on_delete=models.CASCADE)
	sgen = models.CharField(max_length=5,default='h',choices=sg)
	mobileno = models.CharField(max_length=10)
	branch = models.CharField(max_length=10)
	sec = models.CharField(max_length=2)
	image = models.ImageField(null=True,upload_to='studentprofile/')
	

class AddBook(models.Model):
	bname = models.CharField(max_length=100,null=True,blank=True)
	authname = models.CharField(max_length=100,null=True,blank=True)
	bstatus = models.BooleanField(default=False)
	description = models.CharField(max_length=150,null=True,blank=True)
	ncopies = models.PositiveIntegerField(default=1)
	
	
class BookRequest(models.Model):
	c=[
		('Pending','Pending'),
    	('Returned','Returned')
	]
	book = models.ForeignKey(AddBook,on_delete=models.CASCADE)
	due_date = models.DateTimeField(null=True,blank=True)
	requested_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default='')
	requested_by_student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='book_requests_made',null=True)
	return_status = models.CharField(max_length=20,choices=c,default='Pending')
	request_date = models.DateTimeField(auto_now_add=True)
	approved_date = models.DateTimeField(null=True, blank=True)
	fine_amount = models.DecimalField(max_digits=8,decimal_places=2,default=0)
	return_date = models.DateTimeField(null=True, blank=True)
	status_to_approve = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ), default='Pending')
    
    
    








	


def expiry():
    return datetime.today() + timedelta(days=14)




