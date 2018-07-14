# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.


def index(request):
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=KEY_AQUI'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()

    weather_data = []

    cities = City.objects.all()


    # importante, a la hora de hacer un request a la url, parsear el resultado a JSON

    for city in cities:
        
        response = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }
        
        weather_data.append(city_weather)
    
    #print(weather_data)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'index.html', context)