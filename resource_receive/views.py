from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from resource.models import Resource
from django.contrib import messages
from .models import ResourceReceive
from .forms import ResourceReceiveForm

# 📋 List view – Display, search, paginate received resources
def resource_receive_list(request):
    query = request.GET.get("q", "")
    resource_receives = ResourceReceive.objects.all().order_by("id")
    if query:
        resource_receives = resource_receives.filter(project_name__name_of_project__icontains=query)

    paginator = Paginator(resource_receives, 10)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)
    except (EmptyPage, PageNotAnInteger):
        page_obj = paginator.get_page(1)

    return render(request, "resource_receive/resource_receive_list.html", {
        "receives": page_obj,
        "query": query
    })

# 📝 Form view – Create or update resource receive entry
def resource_receive_form(request, id=None):
    receive = get_object_or_404(ResourceReceive, id=id) if id else None

    if request.method == "POST":
        form = ResourceReceiveForm(request.POST, instance=receive)
        if form.is_valid():
            form.save()
            messages.success(request, "Resource entry saved successfully.")
            return redirect("resource_receive_list")
    else:
        form = ResourceReceiveForm(instance=receive)

    return render(request, "resource_receive/resource_receive_form.html", {
        "form": form,
        "receive": receive
    })

# ❌ Delete view – Remove selected entry
def resource_receive_delete(request, id):
    receive = get_object_or_404(ResourceReceive, id=id)
    receive.delete()
    messages.warning(request, f"Resource entry #{receive.id} deleted.")
    return redirect("resource_receive_list")

# 🔁 AJAX endpoint – Get unit of selected resource
def get_resource_unit(request):
    resource_id = request.GET.get("resource_id")
    try:
        resource = Resource.objects.get(id=resource_id)
        return JsonResponse({"unit": resource.resource_unit})
    except (Resource.DoesNotExist, ValueError, TypeError):
        return JsonResponse({"unit": ""})







