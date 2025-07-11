from django.urls import path
from .views import resource_list, resource_form, resource_delete
urlpatterns = [
    path("", resource_list, name="resource_list"),                   # 🔍 List all resources
    path("form/", resource_form, name="resource_create"),            # 🆕 Create a new resource
    path("form/<int:id>/", resource_form, name="resource_edit"),     # ✏️ Edit an existing resource
    path("delete/<int:id>/", resource_delete, name="resource_delete")# ❌ Delete a resource
]
