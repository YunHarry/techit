from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accountapp.models import Registration


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


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/create.html"

class AccountLoginView(LoginView):
    template_name = "accountapp/login.html"

class AccountLogoutView(LogoutView):
    pass