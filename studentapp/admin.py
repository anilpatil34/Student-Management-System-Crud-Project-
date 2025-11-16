from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll','name', 'marks')
    search_fields = ('roll','name', 'marks')
    list_filter = ('roll','name', 'marks')
    ordering = ('roll','marks')
    sortable_by = ('roll','name', 'marks')

