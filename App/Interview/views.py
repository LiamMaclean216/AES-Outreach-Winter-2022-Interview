from django.shortcuts import render

from secrets import token_hex

from .models import *

from django.http import JsonResponse

import json

# Create your views here.

def index(request):
    return render(request, 'Interview/index.html')

def create(request):
    print(request)
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        hex = token_hex(16)
        for i in data["list_ids"]:
            Door.objects.create(door_id = i, token_hex = hex)

        return JsonResponse({'access_token' : hex})


def validate(request, door_id, access_token):
    print(door_id, access_token)
    response = {'is_valid' : Door.objects.filter(door_id=door_id, token_hex=access_token).exists()}

    return JsonResponse(response)