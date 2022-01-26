from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from tab.models import Contents
from forms import ContentsForm, ApplicationsForm


def index(request):
    return render(request, 'tab/index.html')


def board(request):
    contents = Contents.objects.order_by('-create_date')
    context = {'contents': contents}
    return render(request, 'tab/board.html', context)


def board_detail(request, content_id):
    content = get_object_or_404(Contents, pk=content_id)
    context = {'content': content}
    return render(request, 'tab/board_detail.html', context)


@login_required(login_url='tab:login')
def board_post(request):
    if request.method == 'POST':
        form = ContentsForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.create_date = timezone.now()
            content.save()
            return redirect('tab:board')
    else:
        form = ContentsForm()
    context = {'form': form}
    return render(request, 'tab/board_post.html', context)


@login_required(login_url='tab:login')
def board_modify(request, content_id):
    content = get_object_or_404(Contents, pk=content_id)
    if request.method == 'POST':
        form = ContentsForm(request.POST, instance=content)
        if form.is_valid():
            content = form.save()
            return redirect('tab:board')
    else:
        form = ContentsForm(instance=content)
    context = {'content': content}
    return render(request, 'tab/board_post.html', context)


@login_required(login_url='tab:login')
def board_delete(request, content_id):
    content = get_object_or_404(Contents, pk=content_id)
    content.delete()
    return redirect('tab:board')


def recruiting(request):
    if request.method == 'POST':
        form = ApplicationsForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.create_date = timezone.now()
            application.save()
            context = {'name': application.name,
                       'phonenumber': application.phonenumber}
            return render(request, 'tab/recruiting_success.html', context)
    else:
        form = ApplicationsForm()
    context = {'form': form}
    return render(request, 'tab/recruiting.html', context)
