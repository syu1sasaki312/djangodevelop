from django.shortcuts import render
from django.views.generic import TemplateView
from myapp.forms.customer.register import CustomerRegisterForm

class CustomerRegister(TemplateView):
    template_name = 'customer/register.html'
    def __init__(self):
        self.params = {
            "info" : {"type" : 1, "message" : "入力してください。"},
            "form" : CustomerRegisterForm(),
        }

    def get(self,request):
        return render(request, self.template_name, context=self.params)

    def post(self,request):
        self.params["form"] = CustomerRegisterForm(request.POST)
        if self.params["form"].is_valid():
            self.params["form"].save(commit=True)

            self.params["form"] = CustomerRegisterForm()
            self.params["info"] =  {"type" : 1, "message" : "登録しました。"}
        else:
            self.params["info"] =  {"type" : 9, "message" : "入力エラーです。"}

        return render(request, self.template_name, context=self.params)
