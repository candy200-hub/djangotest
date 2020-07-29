from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    return HttpResponse(date)