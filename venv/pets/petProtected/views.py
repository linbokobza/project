from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def home_page(request):
    return render(request, "petProtected/index.html")

def signIn(request):
    return render(request, "petProtected/signIn.html")


def signUp(request):
    return render(request, "petProtected/signUp.html")


def signOut(request):
    pass