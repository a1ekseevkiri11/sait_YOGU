from django.contrib import admin
from .models import (
    Project, 
    Participation,
    MotivationLetters,
    TimePermission,
    Spheres,
    DirectionIdentity,
    Types,
    Order,
)
admin.site.register(Participation)
admin.site.register(MotivationLetters)
admin.site.register(TimePermission)

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ('directionIdentity','spheres','types')

admin.site.register(Order, OrderAdmin)
admin.site.register(Project)
admin.site.register(Spheres)
admin.site.register(Types)
admin.site.register(DirectionIdentity)