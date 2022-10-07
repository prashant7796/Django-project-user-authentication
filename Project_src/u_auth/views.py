from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.
def HomePage(request):
    return render(request, "home.html")

def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():  
            form.save()  
            messages.success(request, "account created successfully")
            print('user created')
        else:
            print('user not created')
    context = {'form': form}
    return render(request, 'register.html', context)


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            messages.success(request, "user is logged in successfully")
            
            return redirect('/')
        else:
            print("user not created")
            messages.error(request, 'invalid creadentials ')
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')