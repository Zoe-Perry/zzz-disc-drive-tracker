from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def char_view(request):
    return HttpResponse("Hello, world!")