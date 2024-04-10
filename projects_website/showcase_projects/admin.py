from django.contrib import admin
from .models import (
    Project, 
    Participation,
    MotivationLetters,
    RejectionComment,
    TimePermission,
    Spheres,
    DirectionIdentity,
    Types,
)
admin.site.register(Participation)
admin.site.register(MotivationLetters)
admin.site.register(RejectionComment)
admin.site.register(TimePermission)



class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('directionIdentity','spheres','types')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Spheres)
admin.site.register(Types)
admin.site.register(DirectionIdentity)