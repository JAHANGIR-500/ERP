from django.shortcuts import render, redirect, get_object_or_404
from .models import ContractorBill
from .forms import ContractorBillForm

def contractor_bill(request):
    bill_id = request.GET.get('bill_id')  # Get bill_id from the request
    contractor_bill = None

    if bill_id:
        contractor_bill = get_object_or_404(ContractorBill, id=bill_id)  # Get existing record safely

    if request.method == 'POST':
        if 'delete' in request.POST:  # Handle deletion
            if contractor_bill:
                contractor_bill.delete()
                return redirect('contractor_bill')  # Redirect after deletion
            
        form = ContractorBillForm(request.POST, instance=contractor_bill)  # Bind form to existing bill
        if form.is_valid():
            form.save()
            return redirect('contractor_bill')  # Redirect after update/save

    else:
        form = ContractorBillForm(instance=contractor_bill)  # Preload form with the existing bill if editing

    contractor_bills = ContractorBill.objects.all()  # Fetch all bills
    return render(request, 'contractor_bill/contractor_bill.html', {
        'form': form,
        'contractor_bills': contractor_bills,
        'contractor_bill': contractor_bill
    })

