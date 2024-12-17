from django.contrib import admin

from course.models import Course, Subject

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Subject)

