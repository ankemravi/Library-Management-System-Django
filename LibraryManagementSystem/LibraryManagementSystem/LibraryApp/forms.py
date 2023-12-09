from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import *
from image_uploader_widget.widgets import ImageUploaderWidget
# from datetime import date
# from django.utils import timezone


class UsrForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","sid"]
		widgets = {
		  "username":forms.TextInput(attrs={
		  	   "class":"form-control my-2",
		  	   "placeholder":"Username",
		  	}),
		  "sid":forms.TextInput(attrs={
		  	"class":"form-control my-2",
		  	"placeholder":"Unique Id",
		  	}),
		}	

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ["mobileno","branch","sec","sgen","image"]
		label={
			'image': ImageUploaderWidget(),
		}
		widgets = {
		"mobileno" : forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter mobileno",
			}),
		"branch" : forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter branch",
			}),
		"sec" : forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter sec",
			}),
		"sgen":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class UserupdationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name", "last_name" , "email"]
		widgets = {
		"first_name" : forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder" : "First Name",
			}),
		"last_name" : forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder" : "Last Name",
			}),
		"email" : forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder" : "EmailId",
			}),
		}

class AddBookForm(forms.ModelForm):
	class Meta:
		model = AddBook
		fields = ["bname","authname","ncopies","description"]
		widgets = {
		"bname" : forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder" : "Book Name",
			}),
		"authname" : forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder" : "Author Name",
			}),
		"description" : forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder" : "Description of the Book:",
			"rows" : 4,
			"cols" :10,
			}),
		"ncopies" : forms.NumberInput(attrs={
				'class' : 'form-control my-2',
				'placeholder' : 'Enter No.of Copies'
				}),
		}
