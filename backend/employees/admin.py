from django.contrib import admin
from .models import Employee
# Register your models here.

class employeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_id', 'picture', 'thumbnail')
    
admin.site.register(Employee, employeeAdmin)