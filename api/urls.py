from django.urls import path
from .views import get_json_data, get_correct_image_view, get_incorrect_image_view

urlpatterns = [
    path('data/', get_json_data, name='get_json_data'),
    path('correct/', get_correct_image_view, name='get_correct_image_view'),
    path('incorrect/', get_incorrect_image_view, name='get_incorrect_image_view')
]