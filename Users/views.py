from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request,id, name) -> HttpResponse:
    return HttpResponse(f"hi {id} {name}")

