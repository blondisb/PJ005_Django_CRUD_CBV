from django.contrib import admin
from .models import MO_candidates

# Register your models here.
class AD_candidate(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'gender', 'position']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['gender', 'position']
    list_per_page = 5

admin.site.register(MO_candidates, AD_candidate)
