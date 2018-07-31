from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    name = forms.CharField(
        label='收件人姓名',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    phone = forms.CharField(
        label='收件人電話',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    pay = forms.CharField(
        label='付款方式',
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': ''}),
        required=True
    )

    class Meta:
        model = Order
        fields = ['name', 'phone', 'pay']
