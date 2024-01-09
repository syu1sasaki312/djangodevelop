from django import forms
from myapp.models import Customer

class CustomerRegisterForm(forms.ModelForm):
    class Meta():
        model = Customer
        fields = ('name','mail', 'post', 'addr','tel','fax','note', 'public_flag')
        labels = {
            'mail':"メールアドレス",
            'name':"会社名",
            'post':"郵便番号",
            'addr':"住所",
            'tel':"TEL",
            'fax':"FAX",
            'note':"備考",
            'public_flag':"公開"
        }
