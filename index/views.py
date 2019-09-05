from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Progress
from .forms import ProgressForm

_progress_pk = 1

def index(request):
    progress, is_created = Progress.objects.get_or_create(pk=_progress_pk, defaults={'percentage':0})
    percent = progress.percentage
    return render(request, 'index.html', {'percent':percent})

@staff_member_required
def percentage(request):
    progress = get_object_or_404(Progress, pk=_progress_pk)
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress.percentage = form.cleaned_data['percentage']
            progress.save()
            return redirect('index')