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
    response = {'is_valid' : False, 'door_exists' : False}

    try:
        door = Door.objects.get(door_id)
    except DoesNotExist:
        return JsonResponse(response)

    response['door_exists'] = True
    response['is_valid'] = (access_token == door.access_token)

    return JsonResponse(response)