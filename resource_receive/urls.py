from django.urls import path
from .views import (
    resource_receive_list,
    resource_receive_form,
    resource_receive_delete,
    get_resource_unit
)

urlpatterns = [
    path("", resource_receive_list, name="resource_receive_list"),  # Display list with search & pagination
    path("form/", resource_receive_form, name="resource_receive_create"),  # Create new entry
    path("form/<int:id>/", resource_receive_form, name="resource_receive_edit"),  # Edit entry
    path("delete/<int:id>/", resource_receive_delete, name="resource_receive_delete"),  # Delete entry
    path("ajax/get-unit/", get_resource_unit, name="get_resource_unit"),  # AJAX endpoint for unit lookup
    
]

