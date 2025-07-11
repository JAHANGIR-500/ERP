from django.shortcuts import render

def inventory_department_view(request):
    return render(request, 'inventory_department/inventory_department.html')