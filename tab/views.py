from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone

from os import listdir
from random import choice

from tab.models import Contents
from forms import ContentsForm, ApplicationsForm


def _get_random_image():
    images = [image for image in listdir('./static/assets/img/random')]
    return choice(images)


def index(request):
    return render(request, 'tab/index.html')


def board(request):
    page = request.GET.get('page', '1')
    contents = Contents.objects.order_by('-create_date')
    paginator = Paginator(contents, 10)
    context = {'contents': paginator.get_page(page)}
    return render(request, 'tab/board.html', context)


def board_detail(request, content_id):
    content = get_object_or_404(Contents, pk=content_id)
    context = {'content': content, 'bg_img': _get_random_image()}
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
    context = {'form': form, 'bg_img': _get_random_image()}
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
    context = {'form': form, 'content': content, 'bg_img': _get_random_image()}
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
            return redirect('tab:recruiting_success')
    else:
        form = ApplicationsForm()
    context = {'form': form}
    return render(request, 'tab/recruiting.html', context)


def recruiting_success(request):
    return render(request, 'tab/recruiting_success.html')


def notfound(request, exception):
    return render(request, 'notfound.html')
