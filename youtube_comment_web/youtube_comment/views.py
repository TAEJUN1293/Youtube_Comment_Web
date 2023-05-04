from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.
def main(request):
    all_video = Video.objects.all()
    context = {'first_video': all_video[0]}
    return render(request, 'youtube_comment/main.html', context)

def detail(request):
    all_video = Video.objects.all()
    context = {'first_video': all_video[0].data}
    return render(request, 'youtube_comment/detail.html', context)