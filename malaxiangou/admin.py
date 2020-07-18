from django.contrib import admin

# Register your models here.
from .models import Social
admin.site.site_header = "Ma Thi Bu Sar Mal"
admin.site.site_title = "Food Admin Portal"
admin.site.index_title = "Welcome to Wat Gyi"

class SocialAdmin(admin.ModelAdmin):
	list_display = ['title','author','date']
	list_filter = ['date']
	search_fields = ['title',]










admin.site.register(Social,SocialAdmin)
