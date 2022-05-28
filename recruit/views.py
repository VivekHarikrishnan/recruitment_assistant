from django.shortcuts import render


def index(request):
    return render(request, "recruit/index.html")


def home(request):
    return render(request, "recruit/home.html")
