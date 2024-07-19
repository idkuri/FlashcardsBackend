from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import read_json_file

@api_view(['GET'])
def get_json_data(request):
    data = read_json_file('chinese.json')
    return Response(data)