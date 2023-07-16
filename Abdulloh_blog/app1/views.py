from datetime import date

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *


def blog(request):
    if request.method=='POST':
        searched=request.POST.get('search')
        result=Blog.objects.filter(title__contains=searched)
        return redirect('/blog/')
    p=Paginator(Blog.objects.all(), 3)
    page=request.GET.get('page')
    pagination_result=p.get_page(page)
    nums="a"*pagination_result.paginator.num_pages

    data={
        'Blog': pagination_result,
        'Blog_recent':Blog.objects.all().order_by('-date')[:5],
        'Categories':Category.objects.all(),
        "Nums":nums,
        "Tag": Tags.objects.all(),
    }

    return render(request,'blog.html',data)

def blog_single(request,a):
    singel = Blog.objects.get(id=a)
    if request.method =='POST':
        n=request.POST.get('name')
        c=request.POST.get('comment')
        # i=request.FILES.get('img')
        Comment.objects.create(name=n,text=c,blog=singel)
        return redirect(f'/blog-single/{a}/')


    data={
        'Single':singel,
        'Comments':Comment.objects.filter(blog=singel),
        'Comment_len':len(Comment.objects.filter(blog=singel)),
        'Blog_recent': Blog.objects.all().order_by('-date')[:5],
        "Tag": Tags.objects.all(),
        "Categories": Category.objects.all(),
    }

    return render(request,'blog-single.html',data)

def blog_filter(request,a):
    g=Category.objects.get(id=a)
    data={
        "Blog_filter":Blog.objects.filter(category=g),
        "Categories":Category.objects.all(),
        'Blog_recent': Blog.objects.all().order_by('-date')[:5],
        "Tag":Tags.objects.all(),
    }
    return render(request,'blog-filter.html',data)

def blog_tag(request,a):
    t=Tags.objects.get(id=a)
    data = {
        "Blog_filter": Blog.objects.filter(tag=t),
        "Categories": Category.objects.all(),
        'Blog_recent': Blog.objects.all().order_by('-date')[:5],
        "Tag": Tags.objects.all(),
    }
    return render(request,"blog-tag.html",data)