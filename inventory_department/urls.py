from django.urls import include, path
from .views import inventory_department_view
urlpatterns = [
    path('', inventory_department_view, name='inventory_department'),
    path('material/', include('material.urls')),  # ✅ Ensures projects are accessible
    path('material_receive/', include('material_receive.urls')),  # ✅ Ensures projects are accessible
]
