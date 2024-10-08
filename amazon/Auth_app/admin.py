from django.contrib import admin
from . models import Contact
# Register your models here.

# admin.site.register(Contact)
@admin.register(Contact)
class ContactModel(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
