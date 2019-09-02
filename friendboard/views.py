from django.shortcuts import render, redirect
from friendboard.models import Post
from friendboard.forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator
# 술친구 views.py

def friendboard(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    post_list = paginator.get_page(page)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/friendboard/')
    else:
        form = PostForm()
    return render(request,'friendboard.html',{'post_list':post_list,'form':form})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('/friendboard/')
    else:
        form = PostForm()
    return render(request, 'friendboard.html',{'forms':forms})

def post_delete(request, pk):
    valpw = request.POST['valpw']
    post = Post.objects.get(pk=pk)
    if post.password == valpw :
        post.delete()
        messages.info(request, '게시물 삭제에 성공했습니다.')
    else :
        messages.error(request, '패스워드가 다릅니다.')
    return redirect('/friendboard/')
    