from django.contrib import admin
from .models import (
    Customer,
    Lecturer,
    Student
)
from django.contrib.auth.models import Permission

admin.site.register(Customer)
admin.site.register(Student)
admin.site.register(Lecturer)
