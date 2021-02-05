from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')
  
def profile(request):
  return render(request, 'User/profile.html')

def signup(request):
  return render(request, 'Registration/signup.html')