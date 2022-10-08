from django.shortcuts import render
# Create your views here.

def home(incoming):
    return render(incoming, 'home.html')
