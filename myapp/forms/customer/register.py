from django import forms
from myapp.models import Customer
from myapp.business.my_validators import MyValidators

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
        error_messages = {
            'mail': {
                'unique': 'メールアドレスが重複しています。',
            },
        }

    def clean_tel(self):
        rtn = self.cleaned_data['tel']
        if MyValidators.isTelephoneNumber(rtn) is False:
            raise forms.ValidationError('電話番号を正しく入力してください。(ハイフン付)')
        return rtn

    def clean_fax(self):
        rtn = self.cleaned_data['fax']
        if MyValidators.isFaxNumber(rtn) is False:
            raise forms.ValidationError('Fax番号を正しく入力してください。(ハイフン付)')
        return rtn
