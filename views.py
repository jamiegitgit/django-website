import requests
from django.http import HttpResponse
from django.shortcuts import render

#if i was going to autogenerate the list of pages, where would that code go?

def index(request):
    context = {
    }
    print("at the index")
    return render(request, 'index.html' , context)


def about(request):
    context = {
    }
    print("at the about page")
    return render(request, 'about.html', context)

def gallery(request):
    context = {
    }
    print("at the gallery page")
    return render(request, 'gallery.html' , context)

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)
