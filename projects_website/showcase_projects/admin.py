from django.contrib import admin
from .models import (
    Project, 
    Participation,
    MotivationLetters,
    RejectionComment,
    TimePermission,
)
admin.site.register(Project)
admin.site.register(Participation)
admin.site.register(MotivationLetters)
admin.site.register(RejectionComment)
admin.site.register(TimePermission)