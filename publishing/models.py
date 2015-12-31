from django.db import models
from django import forms
# Create your models here.

class Books(models.Model):
	title=models.CharField(max_length=200)
	year=models.PositiveIntegerField(null=True,blank=True)
	description=models.TextField(null=True,blank=True)
	author=models.ForeignKey('Author')
	img=models.ImageField(upload_to='books')
	created=models.DateTimeField(auto_now=True)
	#modified=models.DateTimeField(auto_now_add=True) -- only add 1 times
	def __str__(self):
		return self.title
	
class Author(models.Model):
	name=models.CharField(max_length=200)
	slug=models.SlugField(max_length=255,unique=True)
	life=models.TextField(null=True,blank=True)
	def __str__(self):
		return self.name
		
class Pizza(models.Model):
	name=models.CharField(max_length=200)
	topping=models.ManyToManyField('Topping')
	def __str__(self):
		return self.name
	
class Topping(models.Model):
	name=models.CharField(max_length=200)
	def __str__(self):
		return self.name
		
class Recipe(models.Model):
	pizza=models.OneToOneField('Pizza')
	name=models.TextField()
	def __str__(self):
		return self.pizza.name
		
class ContactForm(forms.Form):
	name=forms.CharField(label='Your Name',required=True,max_length=155,help_text='Maximum 155 charachters',error_messages={
		'required':'Please enter Name'
	})
	email=forms.EmailField(label='Your Email',initial='Email address',error_messages={
		'required':'Please Enter Email'
	},required=True)
	
	result=forms.CharField(label='Result',required=False,max_length=155,disabled=True)
	
	file=forms.FileField(label='Choose your file name',required=False)
	
	subject=forms.CharField(label='Your Subject',required=True,widget=forms.Textarea)
	
class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields=('name','slug','life')
		widgets={
			'life':forms.Textarea(attrs={'class':'jeditor'})
		}