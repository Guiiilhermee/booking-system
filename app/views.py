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
    template_name = 'account/base.html'
    
    
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

            messages.success(request, "Your appointment has been created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'account/create-record.html', context=context)


# - Update an appointment

@login_required(login_url='login')
def update_record(request, pk):
    
    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your appointment has been updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'account/update-record.html', context=context)


# - Read / View a singular record

@login_required(login_url='login')
def singular_record(request, pk):
    
    all_records = Record.objects.get(id=pk)
    
    context = {'record':all_records}
    
    return render(request, 'account/view-record.html', context=context)


# - Delete an appointment

@login_required(login_url='login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)
    
    record.delete()
    
    messages.success(request, "Your appointment has been deleted!")
    
    return redirect("dashboard")






# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("login")