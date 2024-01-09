from django.forms import Form
from django import forms

class CustomerSearchForm(Form):

    name = forms.CharField(
        initial='',
        label='顧客名',
        required = False,
        max_length=50,
    )

    mail = forms.CharField(
        initial='',
        label='メールアドレス',
        required = False,
        max_length=50,
    )

    addr = forms.CharField(
        initial='',
        label='住所',
        required = False,
        max_length=200,
    )

    tel = forms.CharField(
        initial='',
        label='電話番号',
        required = False,
        max_length=20,
    )
