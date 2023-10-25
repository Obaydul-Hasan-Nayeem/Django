from django.contrib import admin
from .models import University, Department, Course, Question

admin.site.register(University)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Question)
