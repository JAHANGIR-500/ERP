from django.urls import include, path
urlpatterns = [
    path('', include('home.urls')),  # Make sure this is included
]
