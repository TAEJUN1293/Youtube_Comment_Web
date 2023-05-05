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
    category_id = request.GET.get('category', None)
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        category = None
    category_list = Category.objects.all()
    video_list = []
    videos = Video.objects.filter(categories=category_id)
    for video in videos:
        comment_list = Comment.objects.filter(video_id=video)
        keyword = Keyword.objects.get(video_id=video)
        keyword_list = keyword.keyword.split(' ')
        video_list.append([video, comment_list, keyword_list])
    context = { 'category': category, 'category_list': category_list, 'video_list': video_list}
    return render(request, 'youtube_comment/detail.html', context)