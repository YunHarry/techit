from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm, CustomUserCreationForm
from accountapp.models import Registration
from articleapp.models import Article
from subscribeapp.models import Subscription



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
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/create.html"


class AccountLoginView(LoginView):
    template_name = "accountapp/login.html"


class AccountLogoutView(LogoutView):
    pass

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    template_name = "accountapp/detail.html"
    context_object_name = "target_user"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.object)

        return super().get_context_data(object_list=object_list,
                                        **kwargs)

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    template_name = "accountapp/update.html"
    context_object_name = "target_user"

    def get_success_url(self):
        return reverse("accountapp:detail", kwargs={"pk": self.kwargs["pk"]})

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    template_name = "accountapp/delete.html"
    context_object_name = "target_user"
    success_url = reverse_lazy("accountapp:hello_world")
