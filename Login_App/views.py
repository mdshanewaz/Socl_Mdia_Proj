from django.shortcuts import render, HttpResponseRedirect
from Login_App.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy

# Create your views here.

def signup(request):
    form = CreateUserForm
    registered = False

    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            registered = True
            pass 

    return render(request, 'Login_App/signup.html', context={'title':'SignUp . Instagram', 'form':form, 'registered':registered})        