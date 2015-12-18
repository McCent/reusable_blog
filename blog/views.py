from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import BlogPostForm
from django.shortcuts import redirect

def post_list(request):

    posts  = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blog/blogtests.html", {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1 # clock up the number of post views
    post.save()
    return render(request, "blog/postdetail.html",{'post':post})

def pop_post(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:5]
    return render(request, "blog/blogtests.html", {'posts': posts})

def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', id=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/blogpostform.html', {'form':form})
"""
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    """