from .models import (
    Project,
    DirectionIdentity,
    Spheres,
    Types,
    Lecturer
)
import django_filters
from django import forms


class ProjectFilter(django_filters.FilterSet):
    directionIdentity = django_filters.ModelMultipleChoiceFilter(
        field_name='directionIdentity__title',  # поле по которому будет фильтроваться
        to_field_name='title',
        queryset=DirectionIdentity.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # указываем, что нужно использовать чекбоксы
    )

    customer_type = django_filters.ChoiceFilter(
        choices=Project.CUSTOMER_TYPE, 
        widget=forms.RadioSelect
    )

    spheres = django_filters.ModelMultipleChoiceFilter(
        field_name='spheres__title',  # поле по которому будет фильтроваться
        to_field_name='title',
        queryset=Spheres.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # указываем, что нужно использовать чекбоксы
    )

    types = django_filters.ModelMultipleChoiceFilter(
        field_name='types__title',  # поле по которому будет фильтроваться
        to_field_name='title',
        queryset=Types.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # указываем, что нужно использовать чекбоксы
    )

    lecturer = django_filters.ModelChoiceFilter(
        field_name='lecturer',
        queryset=Lecturer.objects.all(),
        empty_label="Все"
    )

    customer_type.field.empty_label = "Все"
    class Meta:
        model = Project
        fields = ['lecturer', 'customer_type', 'types', 'directionIdentity', 'spheres']