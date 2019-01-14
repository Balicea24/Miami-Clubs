from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .MiamiClubsEvents import getInfo
from .models import UserIP
import datetime
import os
import socket

def club(request, club):
    clubName = club
    events = getInfo(str(club))
    client_ip(request)

    return TemplateResponse(request, 'events.html',
                            {"events": events,
                            "clubName": clubName,})

def index(request):
    client_ip(request)
    return TemplateResponse(request, 'eventshome.html')

def client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')

    if UserIP.objects.filter(ip_address=ip).exists():
        request_count = UserIP.objects.filter(ip_address=ip).get().number_requests
        UserIP.objects.filter(ip_address=ip).update(last_visit = datetime.datetime.now(), number_requests = request_count + 1)

    else:
        user = UserIP()
        user.ip_address = ip
        user.last_visit = datetime.datetime.now()
        user.number_requests += 1
        user.save()
