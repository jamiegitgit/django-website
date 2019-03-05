import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    index= open("templates/index.html").read()
    context = {
        'content': index,
    }
    print("at the index")
    return render(request, 'base.html' , context)


def about(request):
    about = open("templates/about.html").read()
    context = {
        'content': about, 
    }
    return render(request, 'headerfooter.html', context)

def gallery(request):
    gallery = open("templates/gallery.html").read()
    context = {
        'content': gallery,
    }
    return render(request, 'headerfooter.html' , context) #need to extend with base

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)
