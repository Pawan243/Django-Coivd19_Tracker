from django.shortcuts import render
import requests
import json

# Create your views here.

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"india"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "a57eb63de0mshe9f61a492b666fdp1b78b5jsn8f080d816fcd"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    data = response['response']

    d = data[0]

    print(d)

    context = {
        'all': d['cases']['total'],
        'recovered':d['cases']['recovered'],
        'deaths':d['deaths']['total'],
        'new': d['cases']['new'],
        'critical':d['cases']['critical']
    }
    return render(request, 'index.html',context) 