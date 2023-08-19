from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
    