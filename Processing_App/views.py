from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import ImageForm


def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    return render(request, 'Processing_App/index.html', {'form': form})


class HomeView(generic.DetailView):
    template_name = 'Processing_App/index.html'


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
