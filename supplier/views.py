from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from .models import Supplier
from .forms import SupplierForm

# List view – Display, filter, and paginate suppliers
def supplier_list(request):
    query = request.GET.get("q", "")
    suppliers = Supplier.objects.all().order_by("id")
    if query:
        suppliers = suppliers.filter(name_of_supplier__icontains=query)

    paginator = Paginator(suppliers, 10)
    page_number = request.GET.get("page")
    try:
        suppliers_page = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        suppliers_page = paginator.get_page(1)

    return render(request, "supplier/supplier_list.html", {
        "suppliers": suppliers_page,
        "query": query
    })

# Create & Update view – Handle supplier form
def supplier_form(request, id=None):
    supplier = get_object_or_404(Supplier, id=id) if id else None

    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier saved successfully.")
            return redirect("supplier_list")
    else:
        form = SupplierForm(instance=supplier)

    return render(request, "supplier/supplier_form.html", {"form": form})

# Delete view – Remove supplier entry
def supplier_delete(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    supplier.delete()
    messages.warning(request, f"Supplier '{supplier.name_of_supplier}' deleted.")
    return redirect("supplier_list")
