from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'todo/signup.html')


def home(request):
    return render(request, 'todo/home.html')