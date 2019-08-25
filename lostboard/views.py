from django.shortcuts import render, redirect
from django.http import Http404
from .models import LostPost, Comment
from .forms import LostPostForm

# 분실물 views.py

def lostboard(request):
    lostposts = LostPost.objects.all()
    form = LostPostForm()
    return render(request,'lostboard.html', {'lostposts':lostposts, 'form':form})

def createlost(request):
    if request.method == 'POST':
        form = LostPostForm(request.POST, request.FILES)
        if form.is_valid():
            lostpost = form.save(commit=False)
            lostpost.save()
        else:
            print(form.errors)
            raise Http404("form is not valid")
        return redirect('lostboard:detail', lostpost.pk)
    else:
        raise Http404("Wrong Access")

def detail(request, pk):
    try:
        lostpost = LostPost.objects.get(pk=pk)
    except LostPost.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'lostdetail.html', {'lostpost': lostpost})