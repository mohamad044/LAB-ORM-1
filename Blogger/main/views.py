from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Post
# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def create_post_view(request:HttpRequest):
    if request.method == 'POST':
        new_post = Post(title=request.POST['title'],content=request.POST['content'],published_at=request.POST['published_at'])
        new_post.save()
    return render(request,'create_post.html')

def dark_mode_view(request:HttpRequest):
    referer = request.META.get('HTTP_REFERER', '/')
    response = redirect(referer)
    current_mode = request.COOKIES.get('dark_mode')
    
    if current_mode == 'true':
        response.set_cookie('dark_mode', 'false')
    else:
        response.set_cookie('dark_mode', 'true')
    return response