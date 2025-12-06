"""
URL routing for API endpoints.
"""

from django.urls import path
from .views import QueryView, DebugView

app_name = 'api'

urlpatterns = [
    path('query/', QueryView.as_view(), name='query'),
    path('debug/', DebugView.as_view(), name='debug'),
]
