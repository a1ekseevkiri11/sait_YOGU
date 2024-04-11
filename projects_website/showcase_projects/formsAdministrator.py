from django import forms

from .models import Project

class AcceptProjectForm(forms.Form):
    pass

class RejectProjectForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, required=False)


class ProjectForm(forms.ModelForm):

    
    class Meta:
        model = Project
        fields = ['place', 'lecturer', 'customer_type']
    