from django.shortcuts import render
from django.http import HttpResponse

# Sample View to test the flow
def index(request):
    return HttpResponse("Hell0, Iam Vignesh 😍")
