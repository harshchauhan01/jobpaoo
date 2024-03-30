from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Jobpaoo | Admin"
class job_admin(admin.ModelAdmin):
    list_display=['full_name','father_name','email','mobile_no','age','address','cv']
class jobsad(admin.ModelAdmin):
    list_display=['job_head','job_location']
admin.site.register(Details,job_admin)
admin.site.register(Jobs,jobsad)