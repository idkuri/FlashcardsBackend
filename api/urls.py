from django.urls import path
from .views import get_json_data

urlpatterns = [
    path('data/', get_json_data, name='get_json_data'),
]