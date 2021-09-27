from django.shortcuts import render

from secrets import token_hex

from .models import *

from django.http import JsonResponse


# Create your views here.

def create(request, list_ids):
    hex = token_hex(16)
    for i in list_ids:
        Door.objects.create(door_id = i,token_hex  = hex)

    return JsonResponse({'access_token' : hex})


def validate(request, door_id, access_token):
    response = {'is_valid' : False, 'door_exists' : False}

    try:
        door = Door.objects.get(door_id)
    except DoesNotExist:
        return JsonResponse(response)

    response['door_exists'] = True
    response['is_valid'] = (access_token = door.access_token)

    return JsonResponse(response)