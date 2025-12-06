"""
URL configuration for realestate_api project.
"""

from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
]
