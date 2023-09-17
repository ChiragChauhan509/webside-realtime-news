import requests
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    records = {}
    url = requests.get("https://inshorts.me/news/all?offset=0&limit=21")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request,'home.html',records)
    3
def first(request):
    records = {}
    url = requests.get("https://inshorts.me/news/top?offset=0&limit=21")
    inshorts_data = url.json()
    records['top'] = inshorts_data
    return render(request,'first.html',records)

def treding(request):
    records = {}
    url = requests.get("https://inshorts.me/news/trending?offset=0&limit=21")
    my = url.json()
    records['treding'] = my
    return render(request,'treding.html',records)

def science(request):
    records = {}
    url = requests.get("https://inshorts.me/news/topics/science")
    my = url.json()
    records['science'] = my
    return render(request,'science.html',records)

def enter(request):
    records = {}
    url = requests.get("https://inshorts.me/news/topics/entertainment")
    my = url.json()
    records['enter'] = my
    return render(request,'enter.html',records)

def sport(request):
    records = {}
    url = requests.get("https://inshorts.me/news/topics/sports")
    my = url.json()
    records['sport'] = my
    return render(request,'sport.html',records)

