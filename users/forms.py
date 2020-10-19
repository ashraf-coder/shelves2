from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from shelvesapp.models import Business


class UserForm(UserCreationForm):
    email = forms.EmailField()


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ["business_name", "NIN", "location", "contact"]


class CategoryForm(forms.Form):
    CHOICES = (
        (1, "phones"),
        (2, "shoes"),
        (3, "laptops")
    )
    categories = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)