
# Register your models here.
from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'bhk', 'timeline', 'budget', 'submitted_at']
    list_filter = ['bhk', 'timeline', 'budget']
    ordering = ['-submitted_at']


# python manage.py makemigrations
# python manage.py migrate