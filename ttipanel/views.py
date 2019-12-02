from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from.models import Paulapplication

# Create your views here.
def home(request):
    return render (request, "index.html",{})

@login_required(login_url='/login/')
def dash(request):
    return render(request, "dash.html", {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have successfully login !'))
            return redirect("dash")
            #if request.user.groups.filter(name="field_office").exists():
                # user is an admin
                #return redirect("field_office")
            #else:
        else:
            messages.success(request, ('Invaild login'))
            return redirect('login')
    else:
        return render(request, "login.html",{})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out !'))
    return redirect ('home')

@login_required(login_url='/login/')
def field_office(request):
    return render (request, "field_office.html",{})

@login_required(login_url='/login/')
def paulapplication(request):
    return render (request, "paulapplication.html",{})

def Paulapplication(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showpaul')
            except:
                pass
    else:
        form = ProfileForm()
    return render(request,'field_office.html',{'form':form})

def showpaul(request):
    profiles = Paulapplication.objects.all()
    return render(request,"showpaul.html",{'profiles':profiles})
