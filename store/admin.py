from django.contrib import admin

from .models import Artist, Contact, Album, Booking
# Register your models here.

#admin.site.register(Artist, Contact)

@admin.register(Artist, Contact, Album, Booking)
class AppAdmin(admin.ModelAdmin):
    pass
