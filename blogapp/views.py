from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    apps = Blog.objects
    return render(request, 'home.html', {"posts": apps})

def detail(request, a):
    post = get_object_or_404(Blog, pk=a)
    return render(request, 'detail.html', {'details': post})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['top']
    blog.body = request.POST['bottom']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, b):
    destroy = get_object_or_404(Blog, pk=b)
    destroy.delete()
    return redirect('home')

def update(request, c):
    text = get_object_or_404(Blog, pk=c)
    return render(request, 'update.html', {'updates': text})

def edit(request, d):
    edit = Blog.objects.get(pk=d)
    edit.title = request.POST['top']
    edit.body = request.POST['bottom']
    edit.pub_date = timezone.datetime.now()
    edit.save()
    return redirect('home')