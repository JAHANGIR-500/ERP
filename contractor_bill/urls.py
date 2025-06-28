from django.urls import path
from .views import contractor_bill
urlpatterns = [
    path('erp_project/contractor_bill/', contractor_bill, name='contractor_bill'),
]


