from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib import messages
from .forms import CreateUserForm, LoginForm



class HomeTemplateView(TemplateView):
    template_name = 'account/home.html'
    
    
# - Register a user

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("my-login")

    context = {'form':form}

    return render(request, 'account/register.html', context=context)
    
