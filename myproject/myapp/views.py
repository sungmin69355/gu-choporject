from django.shortcuts import render ,get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from accounts.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def write_diary(request):
    return render(request, 'write_diary.html')

@csrf_exempt
def view_diary(request):
    return render(request, 'view_diary.html')