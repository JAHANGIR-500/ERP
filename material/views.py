from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Material
from .forms import MaterialForm
# 📋 List view – Display, filter, and paginate materials
def material_list(request):
    query = request.GET.get("q", "")
    materials = Material.objects.all().order_by("id")
    if query:
        materials = materials.filter(name_of_material__icontains=query)

    paginator = Paginator(materials, 10)
    page_number = request.GET.get("page")
    try:
        materials_page = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        materials_page = paginator.get_page(1)

    return render(request, "material/material_list.html", {
        "materials": materials_page,
        "query": query
    })
# ✏️ Create & Update view – Handle form for adding/editing materials
def material_form(request, id=None):
    material = get_object_or_404(Material, id=id) if id else None

    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, "Material saved successfully.")
            return redirect("material_list")
    else:
        form = MaterialForm(instance=material)
    return render(request, "material/material_form.html", {"form": form})
# ❌ Delete view – Remove material entry
def material_delete(request, id):
    material = get_object_or_404(Material, id=id)
    material.delete()
    messages.warning(request, f"Material '{material.name_of_material}' deleted.")
    return redirect("material_list")

