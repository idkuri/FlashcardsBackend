from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse, Http404
from .utils import read_json_file
import os

@api_view(['GET'])
def get_json_data(request):
    data = read_json_file('chinese.json')
    return Response(data)


@api_view(['GET'])
def get_correct_image_view(request):
    try:
        file_path = os.path.join(os.path.dirname(__file__), "correct.png")
        return FileResponse(open(file_path, 'rb'), content_type='image/png')
    except FileNotFoundError:
        raise Http404("Image not found")

@api_view(['GET'])
def get_incorrect_image_view(request):
    try:
        file_path = os.path.join(os.path.dirname(__file__), "incorrect.png")
        return FileResponse(open(file_path, 'rb'), content_type='image/png')
    except FileNotFoundError:
        raise Http404("Image not found")