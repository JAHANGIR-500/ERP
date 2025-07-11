from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Resource
from .forms import ResourceForm
# 🔍 List view – Display, filter, and paginate resources
def resource_list(request):
    query = request.GET.get("q", "")
    resources = Resource.objects.all().order_by("id")
    if query:
        resources = resources.filter(name_of_resource__icontains=query)  # Updated field name
    paginator = Paginator(resources, 10)
    page_number = request.GET.get("page")
    try:
        resources_page = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        resources_page = paginator.get_page(1)
    return render(request, "resource/resource_list.html", {
        "resources": resources_page,
        "query": query
    })
# 📝 Create & Update view
def resource_form(request, id=None):
    resource = get_object_or_404(Resource, id=id) if id else None
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, "Resource saved successfully.")
            return redirect("resource_list")
    else:
        form = ResourceForm(instance=resource)
    return render(request, "resource/resource_form.html", {"form": form})
# ❌ Delete view
def resource_delete(request, id):
    resource = get_object_or_404(Resource, id=id)
    messages.warning(request, f"Resource '{resource.name_of_resource}' deleted.")  # Updated field
    resource.delete()
    return redirect("resource_list")







