from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.core.paginator import Paginator

# Create your views here.


# def post_list(request):
#     posts = Post.objects.filter(published_date__lte = timezone.now())

#     return render(request, 'blog/post_list.html', {'posts':posts})


def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    p = Paginator(posts,3)

    page_number = request.GET.get('page') #1
    page_obj = p.get_page(page_number)  # <Page 1 of 2>
    
    return render(request,'blog/post_list.html',{'page_obj':page_obj})


def post_detail(request , pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request ,'blog/post_detail.html' , {'post':post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail' , pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


# def post_draft_list(request):
#     posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
#     return render(request , 'blog/post_draft_list.html',{'posts':posts})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    p= Paginator(posts,3)

    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    
    return render(request , 'blog/post_draft_list.html',{'page_obj':page_obj})

def post_publish(request,pk):
    post = get_object_or_404(Post , pk=pk)
    post.publish()
    return redirect('post_detail' , pk=pk)


def post_remove(request,pk):
    post = get_object_or_404(Post , pk=pk)
    post.delete()
    return redirect('post_list')