from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')
    
def signup(request):
    return render(request, 'signup.html')
