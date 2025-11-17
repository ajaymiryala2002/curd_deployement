from django.contrib import admin
from app1.models import employees

class employee_admin(admin.ModelAdmin):
    list_display=['emp_name','emp_id','emp_email']

admin.site.register(employees,employee_admin)
# Register your models here.
