from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from accountapp.models import Registration
from django.urls import reverse

def hello_world(request):
    if request.method == "POST":
        email = request.POST.get('email')

        reg = Registration()
        reg.email = email
        reg.save()

        reg_all = Registration.objects.all()

        return HttpResponseRedirect(reverse("accountapp:hello_world"))

        reg_all = Registration.objects.all()

    temp = "techit"
    return render(request, "accountapp/hello_world.html",
                  context={"temp": temp,
                           "reg_all": reg_all})