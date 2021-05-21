from django.shortcuts import render
from django.utils import timezone
import json

# Create your views here.

def my_first_api_view(request):
    response_data = {
        'method': request.method,
        'datetime': timezone.now().strtime('%y-%m-%d %H:%M')
    }
    response = HttpResponse(json.dumps(response_data))
    response['Content-Type'] = 'application/json'

    return response