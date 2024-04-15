from django import forms

from .models import (
    Project,
    TimePermission
)


class ProjectForm(forms.ModelForm):

    
    class Meta:
        model = Project
        fields = ['place', 'lecturer', 'customer_type']


