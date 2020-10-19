from django import forms
from .models import Phone, Laptop, Shoe, Customer

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ["image", "name", "model", "RAM", "storage", "color"]

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ["name", "storage", "RAM"]

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ["name", "size", "maker"]

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "number"]
