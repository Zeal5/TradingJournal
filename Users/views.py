from django.shortcuts import render
from django.http import HttpResponse
from django.http import response
# Create your views here.


def first(request,id,*args) -> HttpResponse:
    id = [id]
    if args:
        id.append(args)
    print(id)
    context = {
        "id" : id
    }
    return render(request,"users/index.html",context)

