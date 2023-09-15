from django.contrib import admin
from .models import Person, CourseCategory, Course, Registered


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["firstName","lastName"]}),
    ]


class CourseCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]}),
    ]


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["courseCategory", "name", "startDate", "endDate", "quota"]}),
    ]


class RegisteredAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["person", "enlistedCourse"]}),
    ]


admin.site.register(Person, PersonAdmin)
admin.site.register(CourseCategory, CourseCategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Registered, RegisteredAdmin)