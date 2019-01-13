from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .MiamiClubsEvents import getInfo
from .models import UserIP
import datetime
import os

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
    ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxies = x_forwarded_for.split(',')
        while (len(proxies) > 0 and proxies[0].startswith(PRIVATE_IPS_PREFIX)):
            proxies.pop(0)
            if len(proxies) > 0:
                ip = proxies[0]

    if UserIP.objects.filter(ip_address=ip).exists():
        request_count = UserIP.objects.filter(ip_address=ip).get().number_requests
        UserIP.objects.filter(ip_address=ip).update(last_visit = datetime.datetime.now(), number_requests = request_count + 1)

    else:
        user = UserIP()
        user.ip_address = ip
        user.last_visit = datetime.datetime.now()
        user.number_requests += 1
        user.save()
