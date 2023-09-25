from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'index.html')

def User(request):
    username = request.GET['username']
    return render(request, 'user.html', {'name':username})