from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm
from . import urls

# 분실물 views.py

def board(request):
    foundposts = Post.objects.filter(found=True).order_by('-created_at')
    findingposts = Post.objects.filter(found=False).order_by('-created_at')
    form = PostForm()
    return render(request,'lostboard.html', {'foundposts':foundposts, 'findingposts':findingposts, 'form':form})

def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            lostpost = form.save(commit=False)
            lostpost.password = form.cleaned_data['password']
            lostpost.save()
        else:
            print(form.errors)
            raise Http404("form is not valid")
        return redirect('lostboard:detail', lostpost.pk)
    else:
        raise Http404("Wrong Access")

def detail(request, pk):
    lostpost = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    return render(request, 'lostdetail.html', {'post':lostpost, 'form':form})

def createcomment(request, pk):
    lostpost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.lostpost = lostpost
            comment.save()
            return redirect('lostboard:detail', pk=lostpost.pk)
    else:
        raise Http404("Wrong Access")

def deletepost(request, pk):
    lostpost = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if request.POST['valpw'] == lostpost.password:
            lostpost.delete()
            messages.info(request, '게시물 삭제에 성공했습니다.')
        else:
            messages.error(request, '패스워드가 다릅니다.')
        return redirect('lostboard:board')
