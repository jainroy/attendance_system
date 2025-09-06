from django.contrib import admin
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'status')
    list_filter = ('date', 'user', 'status')

admin.site.register(Attendance, AttendanceAdmin)
