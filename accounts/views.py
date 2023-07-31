from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

def signup(request):
    form = SignUpForm()    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('home')
    return render(request,'signup.html',{'form':form})



def login(request):
    return render(request,"yes")


class CustomLoginView(LoginView):
    def get_success_url(self):
        return '/'  # Replace '/' with the desired URL to redirect after login


class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name','last_name','email')
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user