# Register your models here.
from django.contrib import admin
from .models import User, Student, Result, Fee, Note, ReportCard

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Result)
admin.site.register(Fee)
admin.site.register(Note)
admin.site.register(ReportCard)