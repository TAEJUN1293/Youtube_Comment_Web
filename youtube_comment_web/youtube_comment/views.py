from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework import generics


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
    try:
        category_list = Category.objects.all()
    except Category.DoesNotExist:
        category_list = []
    
    video_list = []
    try:
        videos = Video.objects.filter(categories=category_id)
    except Video.DoesNotExist:
        videos = []
    for video in videos:
        try:
            comment_list = Comment.objects.filter(video_id=video)
        except Comment.DoesNotExist:
            comment_list = []
        try:
            keyword = Keyword.objects.get(video_id=video)
            keyword_list = keyword.keyword.split(' ')
        except Keyword.DoesNotExist:
            keyword_list = []
        video_list.append([video, comment_list, keyword_list])
    context = { 'category': category, 'category_list': category_list, 'video_list': video_list}
    return render(request, 'youtube_comment/detail.html', context)


#### API
class PostVideo(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # def post(self, request):
    #     serializers = VideoSerializer(id=request.data["id"], data=request.data["fields"])
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data, status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class PostComment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostKeyword(generics.ListCreateAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer