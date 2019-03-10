import requests
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect

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
    
def contribute(request):
    context = {
    }
    print("at the contribute page")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        mailgun_api_key = os.environ["MAILGUN_API_KEY"]
        email_to = os.environ["EMAIL_TO"]
        request = requests.post(
            "https://api.mailgun.net/v3/sandboxf2abc67e2836444eb33cca99d67c4dd4.mailgun.org/messages",
        auth=("api", mailgun_api_key),
        data={"name": name,
              "from": email,
              "to": email_to,
              "subject": subject,
              "text": message,
              }
        )
        print ('Status: {0}'.format(request.status_code))
        print ('Body:   {0}'.format(request.text))    
        return redirect ("/contribute")
    return render(request, 'contribute.html' , context)

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)
