from .models import (
    Project,
    DirectionIdentity,
    Spheres,
    Types,
    Lecturer,
    Order
)
import django_filters
from django import forms


class OrderFilter(django_filters.FilterSet):
    directionIdentity = django_filters.ModelMultipleChoiceFilter(
        field_name='directionIdentity__title', 
        to_field_name='title',
        queryset=DirectionIdentity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    spheres = django_filters.ModelMultipleChoiceFilter(
        field_name='spheres__title',
        to_field_name='title',
        queryset=Spheres.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    types = django_filters.ModelMultipleChoiceFilter(
        field_name='types__title',
        to_field_name='title',
        queryset=Types.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Project
        fields = ['directionIdentity', 'spheres', 'types']


class ProjectFilter(django_filters.FilterSet):
    
    customer_type = django_filters.ChoiceFilter(
        choices=Project.CUSTOMER_TYPE, 
        widget=forms.RadioSelect,
        label="Тип заказчика",
    )
    customer_type.field.empty_label = "Все"

    lecturer = django_filters.ModelChoiceFilter(
        field_name='lecturer',
        queryset=Lecturer.objects.all(),
        empty_label="Все",
        label="Руководитель",
    )

    directionIdentity = django_filters.ModelMultipleChoiceFilter(
        field_name='order__directionIdentity__title', 
        to_field_name='title',
        queryset=DirectionIdentity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Направление идентичности ЮГУ",
    )

    spheres = django_filters.ModelMultipleChoiceFilter(
        field_name='order__spheres__title',
        to_field_name='title',
        queryset=Spheres.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Сфера проекта",
    )

    types = django_filters.ModelMultipleChoiceFilter(
        field_name='order__types__title',
        to_field_name='title',
        queryset=Types.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Вид проекта",
    )

    class Meta:
        model = Project
        fields = ['lecturer', 'customer_type', 'directionIdentity', 'spheres', 'types']