from django.urls import path
from .views import material_list, material_form, material_delete
urlpatterns = [
    path("", material_list, name="material_list"),  # Display material list with filtering and pagination
    path("form/", material_form, name="material_create"),  # Create a new material
    path("form/<int:id>/", material_form, name="material_edit"),  # Edit an existing material
    path("delete/<int:id>/", material_delete, name="material_delete"),  # Delete a material
]
