from django.shortcuts import render
from.models import UserInfo
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
@csrf_exempt


def saving(request):
    body = json.loads(request.body)
    naam = body["name"]
    email = body ["e"]
    durbash = body ["tel"]

    info = UserInfo(name=naam,email=email,telephone=durbash)
    info.save()

    return JsonResponse ({
        "message" : "user registered succesfully"
    })