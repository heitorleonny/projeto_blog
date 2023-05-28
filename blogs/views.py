from django.shortcuts import render, redirect, get_object_or_404 
from django.urls import reverse
from .models import BlogPost
from .fomrs import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages

def index(request):
    blog_posts = BlogPost.objects.order_by('-date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/index.html', context)

@login_required(login_url='users:login')
def new_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    else:
        form = BlogPostForm()
    return render(request, 'blogs/new_post.html', {'form': form})



@login_required(login_url='users:login')
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    if post.owner != request.user:
        raise Http404
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    else:
        form = BlogPostForm(instance=post)
    
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

def deletar_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    context = {'post': post}
    return render(request, 'blogs/delete_post.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    if post.owner != request.user:
        raise Http404
    
    if request.method == 'POST':
        post.delete()
        return redirect('blogs:index')
    
    context = {'post': post}
    return render(request, 'blogs/delete_post.html', context)
