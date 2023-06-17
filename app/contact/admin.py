from django.contrib import admin

from .models import ContactUs

class Usercontact(admin.ModelAdmin):
    list_display = ('name','email','phone','desc')

admin.site.register(ContactUs,Usercontact)

# Register your models here.
