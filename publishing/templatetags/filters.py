from django import template
#from django.template.loader import render_to_string

register = template.Library()

#render_to_string('inde.html')	
	
@register.filter
def slash(value):
    return value.strip('/')