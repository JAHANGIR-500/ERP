from django.urls import include, path
from .views import construction_department_view
urlpatterns = [
    path('', construction_department_view, name='construction_department'),
    path('project/', include('project.urls')),         # ✅ Ensures projects are accessible
    path('customer/', include('customer.urls')),       # ✅ Ensures customers are accessible
    path('sales_bill/', include('sales_bill.urls')),   # ✅ Ensures sales bills are accessible
    path('supplier/', include('supplier.urls')),       # ✅ Ensures suppliers are accessible
    path('resource/', include('resource.urls')),
    path('resource_receive/', include('resource_receive.urls')),  # ✅ Ensures resource receive entries are accessible
    
]



