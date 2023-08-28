from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm


def blog(request):
    all_blogs = Blog.objects.filter(status='Published').order_by('-submission_date')
    paginator = Paginator(all_blogs, 6)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    context = {
        'all_blogs': paged_blogs,
    }
    return render(request, 'front/blog/blog.html', context)


def blogDetail(request, slug):
    related_blogs = Blog.objects.all().order_by('-submission_date').exclude(slug=slug)
    single_blog = get_object_or_404(Blog, slug=slug)
    single_blog.views = single_blog.views + 1
    single_blog.save()
    context = {
        'related_blogs': related_blogs,
        'single_blog' : single_blog,
    }
    return render(request, 'front/blog/blogDetail.html', context)


@login_required(login_url='login')
def listBlog(request):
    all_blogs = Blog.objects.all().order_by('-submission_date')
    paginator = Paginator(all_blogs, 10)
    page = request.GET.get('page')
    paged_all_blogs = paginator.get_page(page)
    context = {
        'all_blogs': paged_all_blogs,
    }
    return render(request, 'back/blog/listBlog.html', context)


@login_required(login_url='login')
def addBlog(request):
    blog_form = BlogForm()
    if request.method == "POST":
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, 'Your blog has been published.')
            return redirect('listBlogs')

    context = {
        'blog_form': blog_form,
    }
    return render(request, 'back/blog/addBlog.html', context)


@login_required(login_url='login')
def editBlog(request,slug):
    obj = get_object_or_404(Blog, slug=slug)
    blog_form = BlogForm(instance=obj)
    if request.method == "POST":
        blog_form = BlogForm(request.POST, request.FILES, instance=obj)
        if blog_form.is_valid():
            blog_form.save() # Save the form data into the database
            messages.success(request, 'Your blog has been updated.') # Define the message for the user
            return redirect('listBlogs') # Return the response
    context = {
        'obj': obj,
        'blog_form': blog_form,
    }
    return render(request, 'back/blog/editBlog.html', context)
