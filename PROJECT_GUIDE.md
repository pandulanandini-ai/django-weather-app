# Django Weather App - Complete Project Guide

## Step 1

Install Python

## Step 2

Create Virtual Environment

python -m venv venv

Activate

venv\Scripts\activate

## Step 3

Install Django

pip install django

## Step 4

Create Project

django-admin startproject weather_project

## Step 5

Create App

python manage.py startapp weather

## Step 6

Add App inside settings.py

INSTALLED_APPS = [
...
'weather',
]

## Step 7

Create Templates Folder

weather/
    templates/
        weather/

## Step 8

Create Static Folder

weather/static/css/

## Step 9

Create Home Page

home.html

## Step 10

Create Base Template

base.html

## Step 11

Configure Static Files

STATIC_URL

STATICFILES_DIRS

## Step 12

Create Views

Home View

Login View

Dashboard View

Logout View

Register View

## Step 13

Create URLs

urlpatterns

## Step 14

Create Login Form

forms.py

## Step 15

Create Register Form

UserCreationForm

## Step 16

Create Superuser

python manage.py createsuperuser

## Step 17

Run Server

python manage.py runserver

## Step 18

Generate OpenWeatherMap API

https://openweathermap.org/api

## Step 19

Store API Key

views.py

API_KEY="YOUR_API_KEY"

## Step 20

Fetch Weather

requests.get()

## Step 21

Display Weather Data

Temperature

Humidity

Pressure

Feels Like

Wind Speed

Description

## Step 22

Protect Dashboard

@login_required

## Step 23

Register New Users

UserCreationForm

## Step 24

Login Users

authenticate()

login()

## Step 25

Logout Users

logout()

## Step 26

Push to GitHub

git init

git add .

git commit -m "Initial Commit"

git branch -M main

git remote add origin URL

git push -u origin main
