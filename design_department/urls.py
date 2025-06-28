from django.urls import include, path
from .views import design_department_view
urlpatterns = [
    path('', design_department_view, name='design_department'),
    path('task/', include('task.urls')),        # ✅ Ensures projects are accessible
    path('employee/', include('employee.urls')),        # ✅ Ensures projects are accessible
    path('work_plan/', include('work_plan.urls')),  # ✅ Ensures sales bills are accessible
]


