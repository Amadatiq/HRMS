from django.contrib import admin
from .models import employee, Position, Department , Leave , LeaveType 
# Register your models here.

admin.site.register(employee)
admin.site.register(Position)
admin.site.register(Department)
admin.site.register(Leave)
admin.site.register(LeaveType)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ( 'employee' , 'type' , 'from_date', 'to_date')