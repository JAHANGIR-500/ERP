from django.urls import path
from .views import (
    material_receive_list,
    material_receive_form,
    material_receive_delete,
    get_material_details
)

urlpatterns = [
    path("", material_receive_list, name="material_receive_list"),
    path("receive/form/", material_receive_form, name="material_receive_form"),  # for create
    path("receive/form/<int:id>/", material_receive_form, name="material_receive_edit"),  # for edit
    path("delete/<int:id>/", material_receive_delete, name="material_receive_delete"),
    path("ajax/get-details/", get_material_details, name="get_material_details"),
]




