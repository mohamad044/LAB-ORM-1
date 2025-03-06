from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Post
# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def create_post_view(request:HttpRequest):
    if request.method == 'POST':
        new_post = Post(title=request.POST['title'],content=request.POST['content'],published_at=request.POST['published_at'],photo=request.FILES['photo'])
        new_post.save()
    return render(request,'create_post.html')

def post_detail_view(request,post_id):
    
    post = Post.objects.get(pk=post_id)
    return render(request, 'post_detail.html',{'post':post})

def post_update_view(request,post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post_update.html',{'post':post})

def dark_mode_view(request:HttpRequest):
    referer = request.META.get('HTTP_REFERER', '/')
    response = redirect(referer)
    current_mode = request.COOKIES.get('dark_mode')
    
    if current_mode == 'true':
        response.set_cookie('dark_mode', 'false')
    else:
        response.set_cookie('dark_mode', 'true')
    return response