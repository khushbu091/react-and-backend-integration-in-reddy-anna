from django.contrib import admin
from .models import ContactForm

# Register your models here.
from .models import Blog

admin.site.register(Blog)


@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "date")
    search_fields = ("first_name", "email", "phone")