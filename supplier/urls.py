from django.urls import path
from .views import supplier_list, supplier_form, supplier_delete

urlpatterns = [
    path("", supplier_list, name="supplier_list"),  # Display supplier list with filtering and pagination
    path("form/", supplier_form, name="supplier_create"),  # Create a new supplier
    path("form/<int:id>/", supplier_form, name="supplier_edit"),  # Edit an existing supplier
    path("delete/<int:id>/", supplier_delete, name="supplier_delete"),  # Delete a supplier
]
