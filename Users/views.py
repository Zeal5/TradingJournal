from django.shortcuts import render
from django.http import HttpResponse
from django.http import response
import time

# Create your views here.


def first(request,*args, **kwargs) -> HttpResponse:

    context = {
        "id" : [time.time()]
    }
    return render(request,"users/index.html",context)


