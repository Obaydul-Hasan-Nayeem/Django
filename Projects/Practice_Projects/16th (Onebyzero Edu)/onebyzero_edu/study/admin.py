from django.contrib import admin
from .models import University, Department, Course, Question

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Question)


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_format_name')

    def custom_format_name(self, obj):
        return f'{obj.name}'
    custom_format_name.short_description = 'University Name'

admin.site.register(University, UniversityAdmin)