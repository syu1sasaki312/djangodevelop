from django.urls import path
from myapp.views.menu.menu import Menu
from myapp.views.customer.search import CustomerSearch
from myapp.views.customer.register import CustomerRegister

app_name = 'myapp'

urlpatterns = [
    path('', Menu.as_view(), name='menu'),
    path('customers/search', CustomerSearch.as_view()  , name='customers_search'),
    path('customers/input' , CustomerRegister.as_view(), name='customers_input' ),
]
