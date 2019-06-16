from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home(request):
 #   return HttpResponse("Hello World")

def homepage(request):
	return render(request, 'personal/homepage.html')