from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.exceptions import PermissionDenied
from .models import Post, Comment
from .forms import PostForm, CommentForm
from . import urls

# 총학문의게시판 views.py

def board(request):
    qnaposts = Post.objects.all().order_by('-created_at')
    form = PostForm()
    return render(request,'qnaboard.html', {'qnaposts':qnaposts, 'form':form})

def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            qnapost = form.save(commit=False)
            qnapost.password = form.cleaned_data['password']
            qnapost.save()
        else:
            print(form.errors)
            raise Http404("form is not valid")
        return redirect('qnaknuch:detail', qnapost.pk)
    else:
        raise Http404("Wrong Access")

def detail(request, pk):
    try:
        qnapost = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    form = CommentForm()
    if qnapost.public:
        return render(request, 'qnadetail.html', {'qnapost':qnapost, 'form':form})
    if request.method == 'POST':
        if request.POST['password'] == qnapost.password:
            return render(request, 'qnadetail.html', {'qnapost':qnapost, 'form':form})
        raise PermissionDenied("Password is not matched")
    else:
        path = urls.app_name + ":detail"
        return render(request, 'qnapwcheck.html', {'qnapost':qnapost, 'path':path})

def createcomment(request, pk):
    qnapost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.qnapost = qnapost
            comment.save()
            return redirect('qnaknuch:detail', pk=qnapost.pk)
    else:
        raise Http404("Wrong Access")

def deletepost(request, pk):
    try:
        qnapost = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    if request.method == 'POST':
        if request.POST['password'] == qnapost.password:
            qnapost.delete()
            return redirect('qnaknuch:board')
        raise PermissionDenied("Password is not matched")
    else:
        path = urls.app_name + ":deletepost"
        return render(request, 'qnapwcheck.html', {'qnapost': qnapost, 'path':path})
