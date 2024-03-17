from django import forms

class AcceptProjectForm(forms.Form):
    pass

class RejectProjectForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, required=False)