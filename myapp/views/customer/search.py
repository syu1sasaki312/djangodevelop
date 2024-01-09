from django.views.generic import ListView
from django.db.models import Q
from myapp.models import Customer
from myapp.forms.customer.search import CustomerSearchForm

class CustomerSearch(ListView):

    template_name = 'customer/search.html'
    model = Customer
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomerSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        name = self.request.GET.get('name')
        mail = self.request.GET.get('mail')
        addr = self.request.GET.get('addr')
        tel  = self.request.GET.get('tel')
        queryset = Customer.objects.order_by('id')
        if name:
            queryset = queryset.filter(Q(name__icontains=name))
        if mail:
            queryset = queryset.filter(Q(mail__icontains=mail))
        if addr:
            queryset = queryset.filter(Q(addr__icontains=addr))
        if tel:
            queryset = queryset.filter(Q(tel__icontains=tel))
        return queryset
