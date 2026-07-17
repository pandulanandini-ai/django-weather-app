from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from .forms import LoginForm, RegisterForm
import requests


API_KEY = "416814cfd0ec3ccd9c21be21d09031c1"
def home(request):
    return render(request, 'weather/home.html')


def login_view(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('dashboard')

    return render(request, 'weather/login.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):

    weather = None

    if request.method == "POST":

        city = request.POST.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        if response.status_code == 200:

            weather = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"]["speed"],
                "weather": data["weather"][0]["main"],
                "description": data["weather"][0]["description"],
            }

    return render(request, "weather/dashboard.html", {"weather": weather})
def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = RegisterForm()

    return render(request, 'weather/register.html', {'form': form})