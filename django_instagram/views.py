from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts' : posts})

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        post = form.save(commit=False)
        post.save()

        return redirect('detail', post.pk)
    else:
        form = PostForm()
        
        return render(request, 'new.html', {'form' : form})

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('detail', post_pk)
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'post' : post, 'form' : form})

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    comment.delete()
    return redirect('detail', post_pk)
    