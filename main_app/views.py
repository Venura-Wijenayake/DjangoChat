from django.shortcuts import render #, redirect


def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def chats_index(request):
   return render(request, "chats/index.html")

def chats_detail(request):
   return render(request, "chats/detail.html")