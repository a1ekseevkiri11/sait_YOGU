from django import forms
from .models import (
    Order,
    Spheres,
    Types,
    DirectionIdentity
)


class OrderForm(forms.ModelForm):

    directionIdentity = forms.ModelMultipleChoiceField(
        queryset=DirectionIdentity.objects.all(),
        widget=forms.CheckboxSelectMultiple(),  # Используем CheckboxSelectMultiple вместо SelectMultiple
        required=False  # Делаем поле необязательным, если это возможно
    )

    spheres = forms.ModelMultipleChoiceField(
        queryset=Spheres.objects.all(),
        widget=forms.CheckboxSelectMultiple(),  # Используем CheckboxSelectMultiple вместо SelectMultiple
        required=False  # Делаем поле необязательным, если это возможно
    )

    types = forms.ModelMultipleChoiceField(
        queryset=Types.objects.all(),
        widget=forms.CheckboxSelectMultiple(),  # Используем CheckboxSelectMultiple вместо SelectMultiple
        required=False  # Делаем поле необязательным, если это возможно
    )
    
    class Meta:
        model = Order
        fields = ['title', 'description', 'directionIdentity', 'spheres', 'types']
    
