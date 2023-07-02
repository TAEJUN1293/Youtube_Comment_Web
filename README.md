

# Youtube_Comment_Web
<img src="https://img.shields.io/badge/github-181717?style=flat&logo=github&logoColor=white"/> <img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/jupyter-F37626?style=flat&logo=jupyter&logoColor=white"/> <img src="https://img.shields.io/badge/selenium-43B02A?style=flat&logo=selenium&logoColor=white"/> <img src="https://img.shields.io/badge/django-092E20?style=flat&logo=django&logoColor=white"/>



## ✅ 주제 : 유튜브 인기급상승 댓글 분석을 통한 시각화 및 키워드 제공
<br></br>


## ✅ 프로젝트 개요 


### 🎈 프로젝트 내용 
네이버 실시간 검색어 기능이 사라진 현재, 사람들이 가장 많이 사용한다고 할 수 있는 유튜브 기반 인기 급상승 영상에 달린 댓글을 통해
영상 카테고리별 단어 사용 실태와 영상별 키워드를 추출해낸 프로젝트입니다.


### 🎈 프로젝트 기간 
23.05.01 ~ 23.05.05


### 🎈 팀원
|이름|역할|
|:---:|:---:|
|김상희|크롤러, 프론트|
|김태준|크롤러, 벡엔드|
|박경모|크롤러, 백엔드|
|임형우|크롤러, 벡엔드|
|이하윤|크롤러, 프론트|

<br></br>

## ✅ 프로그램 실행 방법

1. clone 명령어로 해당 폴더 복제
```
git clone https://github.com/TAEJUN1293/Youtube_Comment_Web.git
```

2. 가상환경 생성 및 활성화
```
$ py -m venv project-name
$ project-name\Scripts\activate.bat 
```

3. 폴더 이동 및 서버실행
```
$ cd youtube_comment_web 
$ python manage.py runserver
```

<br></br>

## ✅ 프로젝트 진행과정

### 🎈 Crawling
인기 급상승 채널 중 카테고리(최신, 음악, 게임, 영화) 에 한해 올라와 있는 모든 영상들의 데이터 크롤링 및 json으로 가공

< raw data > 크롤링 실행 결과

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
< json_data > 데이터베이스에 저장할 수 있는 포맷으로 가공한 데이터

```
   comment : 	{ video_id : [comments], }
   keyword : 	{ video_id : "keyword", }
     video : 	{ video_id : [ thumbnail_url, title, url, count_of_view, count_of_comment ], }
```



### 🎈 데이터 모델링 & ERD
![image](https://user-images.githubusercontent.com/89377440/236507285-39ff5b4a-456f-4754-8795-a2e35afbdd8e.png)


### 🎈 DB에 데이터 적재 과정

![데이터 적재](https://user-images.githubusercontent.com/89377440/236528050-3ce62579-ef85-4676-8f64-fe12d8066adf.gif)



## ✅ 구현한 웹사이트 

![화면 실행](https://user-images.githubusercontent.com/89377440/236537084-ed06f251-883b-42b0-af39-22b204c3cad1.gif)


## ✅ DB에 적재된 데이터 (확인)

![데이터베이스에 적재됨](https://user-images.githubusercontent.com/89377440/236539552-0d0394e1-4fac-481a-87d7-3e11a8b5f0cf.gif)

