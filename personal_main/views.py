from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(home)


# About Me view
def about(request):
    return render(request, 'personal_main/about.html')