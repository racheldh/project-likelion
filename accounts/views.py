from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def signup(request):
    if request.method == "POST":
        if request.POST['password1']==request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'blog/home.html')
        else:
            return render(request, 'accounts/signup.html', {'error': 'password was not consistent.'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'blog/home.html')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

def logout(request):        
    auth.logout(request)
    return redirect('home')
