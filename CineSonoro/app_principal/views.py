from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Index(request):
 return HttpResponse("Hola Mundo desde Django")
