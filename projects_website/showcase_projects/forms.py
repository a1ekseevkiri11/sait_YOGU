from django import forms
from .models import MotivationLetters

class ConfirmationForm(forms.Form):
    confirmation = forms.BooleanField(label='Вы уверены, что хотите присоединиться к проекту?', required=True)


class MotivationLettersForm(forms.ModelForm):
    class Meta:
        model = MotivationLetters  
        fields = ['letter']  

    def __init__(self, *args, **kwargs):
        super(MotivationLettersForm, self).__init__(*args, **kwargs)
        self.fields['letter'].widget.attrs.update({'accept': '.doc, .docx'})