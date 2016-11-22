from django.contrib import admin
from models import Contactus
# Register your models here.
class ContactusAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display = ('name', 'email', 'description')

admin.site.register(Contactus, ContactusAdmin)