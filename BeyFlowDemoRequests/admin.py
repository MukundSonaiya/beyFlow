from django.contrib import admin
from models import DemoRequest

class DemoRequestAdmin(admin.ModelAdmin):
	list_display = ['fullname','email','message','canReceiveMails']

	def fullname(self, obj):
		return obj.firstName + obj.lastName

admin.site.register(DemoRequest,DemoRequestAdmin)
