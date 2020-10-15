from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    my_context = {
        "text1" : "I Am A ",
        "num" : 13,
        "text2" : "-Year-Old Full Stack Dev",
        "list" : ["i like trains", "do you like trains?"],
    }
    return render(request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "contact.html", {})

def discord_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return redirect('https://discord.gg/6GPjN8C')

def youtube_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return redirect('https://www.youtube.com/channel/UC6vusNTseRpomq7ruox9_0g')

def github_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return redirect('https://github.com/johndoe434')