from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    temp = "techit"
    return render(request, "accountapp/hello_world.html",
                  context={"temp": temp})