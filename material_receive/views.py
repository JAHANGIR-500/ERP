from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.contrib import messages
from .models import MaterialReceive
from .forms import MaterialReceiveForm
from material.models import Material
# 📋 List view – Display, search, paginate received materials
def material_receive_list(request):
    query = request.GET.get("q", "")
    material_receives = MaterialReceive.objects.all().order_by("id")
    if query:
        material_receives = material_receives.filter(project_name__name_of_project__icontains=query)

    paginator = Paginator(material_receives, 10)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)
    except (EmptyPage, PageNotAnInteger):
        page_obj = paginator.get_page(1)
    return render(request, "material_receive/material_receive_list.html", {
        "receives": page_obj,
        "query": query
    })
# 📝 Form view – Create or update material receive entry
def material_receive_form(request, id=None):
    receive = get_object_or_404(MaterialReceive, id=id) if id else None
    if request.method == "POST":
        form = MaterialReceiveForm(request.POST, instance=receive)
        if form.is_valid():
            form.save()
            messages.success(request, "Material receive entry saved successfully.")
            return redirect("material_receive_list")
    else:
        form = MaterialReceiveForm(instance=receive)
    return render(request, "material_receive/material_receive_form.html", {
        "form": form,
        "receive": receive
    })
# ❌ Delete view – Remove selected entry
def material_receive_delete(request, id):
    receive = get_object_or_404(MaterialReceive, id=id)
    receive.delete()
    messages.warning(request, f"Material receive entry #{receive.id} deleted.")
    return redirect("material_receive_list")
# 🔁 AJAX endpoint – Get unit, type, and group of selected material
def get_material_details(request):
    material_id = request.GET.get("material_id")
    try:
        material = Material.objects.get(id=material_id)
        return JsonResponse({
            "unit": material.material_unit,
            "material_type": material.type_of_material,
            "material_group": material.group_of_material
        })
    except (Material.DoesNotExist, ValueError, TypeError):
        return JsonResponse({
            "unit": "",
            "material_type": "",
            "material_group": ""
        })



