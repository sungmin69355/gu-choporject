from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def write_diary(request):
    return render(request, 'write_diary.html')

def view_diary(request):
    return render(request, 'view_diary.html')
