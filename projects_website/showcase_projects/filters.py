from .models import (
    Project,
    DirectionIdentity
)
import django_filters
from django import forms


class ProjectFilter(django_filters.FilterSet):
    # directionIdentity = django_filters.ModelMultipleChoiceFilter(
    #     field_name='directionIdentity__title',  # поле по которому будет фильтроваться
    #     to_field_name='title',
    #     queryset=DirectionIdentity.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,  # указываем, что нужно использовать чекбоксы
    # )
    class Meta:
        model = Project
        fields = ['lecturer']