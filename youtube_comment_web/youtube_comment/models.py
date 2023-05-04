from django.utils import timezone
from django.db import models

# Create your models here.
class Category(models.Model):
    """
    id(PK): varchar(20), category 아이디 (recent, music, game, movie)
    category: varchar(20), category 이름 (ex: 최신)
    videos: 인기 급상승 해당 카테고리 영상 목록 (video id 값)
    """
    id = models.CharField(max_length=20, primary_key=True, editable=False)
    category = models.CharField(max_length=20)
    videos = models.ManyToManyField('Video', through='Trending')

class WordCloud(models.Model):
    """
    id(PK): INT, autoField
    category_id: 연관된 category
    img_src: 이미지 경로
    create_time: 생성일
    """
    category_id = models.OneToOneField('Category', on_delete=models.CASCADE)
    img_src = models.ImageField(upload_to ='images/')
    create_time = models.DateTimeField(default=timezone.now)

class Video(models.Model):
    """
    id(PK): varchar(20), 동영상 아이디
    thumbnail_url: varchar(200), 썸네일 이미지 링크
    title: varchar(150), 동영상 제목
    url: varchar(50), 동영상 링크
    count_of_view: INT, 조회 수
    count_of_comment: INT, 댓글 수
    categories: 연관된 인기 급상승 카테고리 목록
    """
    id = models.CharField(max_length=20, primary_key=True, editable=False)
    thumbnail_url = models.URLField(max_length=200)
    title = models.CharField(max_length=150)
    url = models.URLField(max_length=200)
    count_of_view = models.PositiveBigIntegerField(default=0)
    count_of_comment = models.PositiveBigIntegerField(default=0)
    categories = models.ManyToManyField('Category', through='Trending')

class Comment(models.Model):
    """
    id(PK): INT, autoField
    video_id(FK): varchar(20), 연관된 video
    comment: TEXT, 댓글 내용
    """
    video_id = models.ForeignKey('Video', on_delete=models.CASCADE, null=True)
    comment = models.TextField(blank=True, null=True)

class Keyword(models.Model):
    """
    id(PK): INT, autoField
    video_id(FK): varchar(20), 연관된 video
    keyword: TEXT, 띄어쓰기로 구분된 문자열
    create_time: 생성일
    """
    video_id = models.OneToOneField('Video', on_delete=models.CASCADE, null=True)
    keyword = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(default=timezone.now)

class Trending(models.Model):
    """
    id(PK): INT, autoField
    category_id(FK): varchar(20), 연관된 category
    video_id(FK): varchar(20), 연관된 video
    create_time: 생성일
    """
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=timezone.now)
