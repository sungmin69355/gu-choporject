from django.shortcuts import render ,get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from accounts.models import User
from django.db import IntegrityError
import getpass

# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})

def write_diary(request):
    return render(request, 'write_diary.html')

@csrf_exempt
def view_diary(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'view_diary.html',{'posts':posts})

def create(request):
    posts = Post()
    posts.title = request.GET.get('title','') 
    posts.body = request.GET.get('text','') 
    posts.pub_date = timezone.datetime.now()
    posts.save()
    posts = Post.objects.all().order_by('-id')
    return render(request, 'view_diary.html',{'posts':posts})