from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .forms import MakePostForm, MakeCommentForm
from .models import BlogPost, Comment


# Create your views here.
@login_required
def post_list(request):
    blogs_list = BlogPost.objects.all()
    return render(request, 'blog_app/post_list.html', {'blogs_list': blogs_list})


@login_required
@permission_required('blog_app.add_blogpost')
def make_post(request):
    if request.method == 'POST':
        form = MakePostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            blog_post = BlogPost(user=request.user, title=title, body=body)
            blog_post.save()
            return redirect('blog_app:post_list')
    else:
        form = MakePostForm()

    return render(request, 'blog_app/make_post.html', {'form': form})


@login_required
def post_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    form = MakeCommentForm()
    return render(request, 'blog_app/post_detail.html', {'form': form, 'blog': blog})


@login_required
def make_comment(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    if request.method == 'POST':
        form = MakeCommentForm(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['body']
            comment = Comment(user=request.user, blogpost=blog, body=comment_text)
            comment.save()
    else:
        form = MakeCommentForm()

    return render(request, 'blog_app/post_detail.html', {'form': form, 'blog': blog})
