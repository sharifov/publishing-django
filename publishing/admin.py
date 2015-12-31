from django.contrib import admin

# Register your models here.
from django.conf import settings
from .models import Author,Books,Pizza,Topping,Recipe,AuthorForm

class AuthorAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':['name']}
	list_display=['name','slug']
	search_fields=['name']
	form=AuthorForm
	class Media:
		js=('%sjs/tiny_mce/tiny_mce.js' % settings.STATIC_URL,
			'%sjs/tiny_mce/tiny_mce_inc.js' % settings.STATIC_URL
		)

class BooksAdmin(admin.ModelAdmin):
	class Media:
		js=('%sjs/tiny_mce/tiny_mce.js' % settings.STATIC_URL,
			'%sjs/tiny_mce/tiny_mce_inc.js' % settings.STATIC_URL
		)
	
admin.site.register(Author,AuthorAdmin)
admin.site.register(Books,BooksAdmin)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Recipe)