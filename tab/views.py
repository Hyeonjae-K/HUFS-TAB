import requests

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from tab.models import Contents
from forms import ContentsForm, ApplicationsForm
from config import secret


def _get_image():
    return requests.get('https://api.unsplash.com/photos/random?query=computer&client_id=%s' %
                        secret.UNSPLASH_ACCESS_KEY).json()['urls']['full']


def index(request):
    context = {'bg_img': _get_image()}
    return render(request, 'tab/index.html', context)


def board(request):
    contents = Contents.objects.order_by('-create_date')
    context = {'contents': contents, 'bg_img': _get_image()}
    return render(request, 'tab/board.html', context)


def board_detail(request, content_id):
    content = get_object_or_404(Contents, pk=content_id)
    context = {'content': content, 'bg_img': _get_image()}
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
    context = {'form': form, 'bg_img': _get_image()}
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
    context = {'content': content, 'bg_img': _get_image()}
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
                       'phonenumber': application.phonenumber, 'bg_img': _get_image()}
            return render(request, 'tab/recruiting_success.html', context)
    else:
        form = ApplicationsForm()
    context = {'form': form, 'bg_img': _get_image()}
    return render(request, 'tab/recruiting.html', context)
