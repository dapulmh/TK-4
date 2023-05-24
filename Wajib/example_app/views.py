from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def indexWelcome(request):
    return render(request, 'welcome.html')

def indexLogin(request):
    return render(request, 'loginForm.html')