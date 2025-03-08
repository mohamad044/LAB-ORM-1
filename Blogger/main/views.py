from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Post
from django.db.models import Q

# Create your views here.

def home_view(request):
    posts = Post.objects.all().order_by('-published_at')
    return render(request,'home.html',{'posts':posts})

def create_post_view(request:HttpRequest):
    if request.method == 'POST':
        new_post = Post(title=request.POST['title'],content=request.POST['content'],published_at=request.POST['published_at'],photo=request.FILES['photo'])
        new_post.save()
        return redirect('home_view')
    return render(request,'create_post.html')

def post_detail_view(request,post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post_detail.html',{'post':post})

def post_update_view(request:HttpRequest,post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.published_at = request.POST['published_at']
        if 'photo' in request.FILES: post.photo = request.FILES['photo']
        post.save()
        return redirect('post_detail_view',post_id=post_id)
    
    return render(request, 'post_update.html',{'post':post})

def post_delete_view(request:HttpRequest,post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('home_view')

def dark_mode_view(request:HttpRequest):
    referer = request.META.get('HTTP_REFERER', '/')
    response = redirect(referer)
    current_mode = request.COOKIES.get('dark_mode')
    
    if current_mode == 'true':
        response.set_cookie('dark_mode', 'false')
    else:
        response.set_cookie('dark_mode', 'true')
    return response

def search_post_view(request:HttpRequest):
    if 'search' in request.GET:
        search_query = request.GET.get('search', '')
        posts = Post.objects.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
                                    )
        posts.order_by('-id')
        
    return render(request,'search_post.html',{'posts':posts})