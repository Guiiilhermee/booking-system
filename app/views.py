from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib import messages
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import login


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from .models import Record










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
            return redirect('login')

    context = {'form':form}

    return render(request, 'account/register.html', context=context)

# - Log in the user

def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")

    context = {'form': form}
    return render(request, 'account/login.html', context=context)
        

# - dashboard
 
@login_required(login_url='login')
def dashboard(request):
    
    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'account/dashboard.html', context=context)


# - Create an appointment

@login_required(login_url='login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'account/create-record.html', context=context)




# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("login")