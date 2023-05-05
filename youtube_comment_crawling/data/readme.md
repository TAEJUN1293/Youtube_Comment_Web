크롤링 데이터 저장 공간

```
   comment : 	{ video_id : [comments], }
   keyword : 	{ video_id : "keyword", }
     video : 	{ video_id : [ thumbnail_url, title, url, count_of_view, count_of_comment ], }
```



Column Description

< game - movie > 
```
   category : [최신, 음악, 게임, 영화]
   title : 영상별 제목
   img_url : 영상별 썸네일 이미지
   count_of_views : 영상별 조회수
   url : 영상별 url 
   count_of_comments : 영상별 전체 댓글수
   comments_all : 영상별 크롤링한 전체 댓글 리스트
   scrap_count : 영상별 크롤링한 샘플 댓글수
   comments : 영상별 상위 댓글 30개
   word_frequency : 영상별 크롤링한 댓글 중 모든 키워드 빈도수 
   keyword : 영상별 크롤링한 댓글 중 키워드 상위 30개
   video_id : 영상별 unique id
  
```
