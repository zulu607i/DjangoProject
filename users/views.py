from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
# Create your views here.


def home(request):
    return render(request, 'home.html')


def register_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.userprofile.first_name = form.cleaned_data.get('first_name')
        user.userprofile.last_name = form.cleaned_data.get('last_name')
        user.userprofile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=str(username), password=str(password))
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')





