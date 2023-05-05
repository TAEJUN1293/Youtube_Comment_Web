from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.
def main(request):
    cloud_list = WordCloud.objects.all()
    context = {'word_clouds': cloud_list}
    return render(request, 'youtube_comment/main.html', context)

def detail(request):
    category = request.GET.get('category', None)
    category_list = Category.objects.all()
    video_list = Video.objects.all()
    wordcloud_list = WordCloud.objects.all()
    context = {'category_list': category_list, 'category': category, 'video_list': video_list, 'wordcloud_list': wordcloud_list}
    return render(request, 'youtube_comment/detail.html', context)