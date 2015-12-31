from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from publishing.models import Topping,Pizza,Recipe,ContactForm,Books
from django.contrib.auth.decorators import login_required


def pages(request,tag='index'):
	toppings=Topping.objects.all()
	books=Books.objects.all()
	nav=Pizza.objects.all()
	needed={
		'site_title': 'My Project',
		'menu':toppings,
		'nav':nav,
		'page_title':'Introduction to spark',
		'books':books
	}
	
	if (tag not in 'index') and (tag not in 'contact'):
		target=Pizza.objects.get(name=tag)
		needed['page_title']=target.name
		try:
			page_body=Recipe.objects.get(pizza=target.id).name
		except Recipe.DoesNotExist:
			page_body=''
			
		needed.setdefault('page_body',page_body)
	
	if tag in 'contact':
		#return redirect('/admin/')
		needed['page_title']=tag.capitalize()
		form=ContactForm(request.POST or None,request.FILES or None)
		if form.is_valid():
			from django.core.mail import send_mail
			from django.conf import settings
			
			if request.FILES and request.FILES['file'].size > 0:
				fname=request.FILES['file'].name.split('.')[0]
				fext=request.FILES['file'].name.split('.')[-1]
				open(settings.UPLOAD_ROOT+'/'+fname+'.'+fext,'wb').write(request.FILES['file'].read())
				request.session['upload_file']='Your file Sending'
				return redirect('/contact')
				
			send_mail('Subject here', 'Here is the message.', 'jafar.sharifov@gmail.com',['milad.sharifov@gmail.com'], fail_silently=False)	
			
			#msg='{} \n\r {}'.format(form.cleaned_data['name'],form.cleaned_data['subject'])
			
			'''
			send_mail(
				'Mail from'+settings.BASE_DIR,
				msg,
				form.cleaned_data['email'],
				[settings.EMAIL_HOST_USER],
				fail_silently=True
			)
			'''
		needed.setdefault('contacts',form)
	
	trace='Hello World' if request.META.get('PATH_INFO').strip('/')=='welcome' else 'Index World'
	return render(request,'index.html',needed)