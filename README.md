[TOC]

#	 종합 프로젝트 

>  영화 정보 기반 추천 서비스, 커뮤니티 구성



## INDEX

### 1. 언어

1. Python 3.7+
2. Django 3.X
3. Node 14.15.X
4. vue.js 2.6+



### 2. 도구

	1. vsCode
 	2. Chrom Browser



### 3. 아키텍쳐

	1. Django REST API 서버 & Vue.js



### 4. API 데이터 수집

1. 영화 진흥 위원회
2. 네이버 영화 검색 API
3. TMDB - The Movie Databas
4. Google Youtube 동영상 API



---

## 1. 팀원 정보 및 업무 분담 내역

#### 1) 김진영

- Front-end Design 총괄
- repl.it에서 mock-up 한 후 vue프로젝트에 적용
- BEM을 적용하여 체계적인 CSS 스타일 구축
- UI향상을 위한 Carousel 적용



#### 2) 전의수

- Django REST-Framework 를 이용한 데이터 모델링 및 JSON화 & 백엔드 서버 구축 및 실행
- Django REST-Framework 를 이용한 로그인, 회원가입 데이터베이스 구축
- Axios를 활용한 데이터 크롤링
- 유저 평점을 기반으로 한 영화 추천 알고리즘 구현
- 장르별 영화 추천 알고리즘 구현
- 영화리뷰, 커뮤니티, 댓글 작성 기능 구현(CRUD)
- YOUTUBE API를 활용한 영화 예고편표시
- VueJs를 활용한 front-end 페이지 구축



---

## 2. 목표 서비스 구현 및 실제 구현 정도

1.  목표 서비스

   - [ ] 필수 기능 구현
   - [ ] 반응형 웹 구현
     - 화면의 비율에 맞게 변환되는 반응형 웹 구현
     - carousel을 활용한 반응형 영화데이터 표시
   - [ ] CSS 및 라이브러리를 활용한 웹 사이트 디자인
     - 모달을 이용하여 영화 상세 정보 제공
     - Vuetify를 활용한 전체적인 웹 사이트 디자인
     - Youtube iframe을 활용한 영화 예고편 제공
   - [ ] 평점을 활용한 추천 알고리즘
     - 유저가 영화에 대한 평점을 남긴다.
     - 해당 유저가 선호하는 영화 장르를 선별하기 위한 기준으로 평점 4점 이상의 영화를 정재한다.
     - 평점 4점 이상의 영화 중에 가장 많이 나온 장르를 유저에게 추천한다.
   - [ ] 주식 데이터를 기반으로 한 추천 알고리즘
   - [ ] 별도의 관리자 페이지를 구현하여 영화 데이터 및 유저 관리
   - [ ] 영화 정보에 대한 대화를 나눌수 있도록 커뮤니티 페이지 제공
   - [ ] 소셜커뮤니티 로그인기능 구현

   

2. 실제 구현 정도

   - [x] 필수 기능 구현

   - [x] 반응형 웹 구현

     - 화면의 비율에 맞게 변환되는 반응형 웹 구현
     - carousel을 활용한 반응형 영화데이터 표시

   - [x] CSS 및 라이브러리를 활용한 웹 사이트 디자인

     - 모달을 이용하여 영화 상세 정보 제공
     - Youtube iframe을 활용한 영화 예고편 제공

   - [x] 평점을 활용한 추천 알고리즘

     - 평점을 기반으로 한 영화 추천 
     - 네이버 및 TMDB rating 별 영화 추천
     - 장르별 영화 추천

   - [x] 별도의 관리자 페이지를 구현하여 영화 데이터 및 유저 관리

   - [x] 영화 정보에 대한 대화를 나눌수 있도록 커뮤니티 페이지 제공

     - 로그인한 사용자만 커뮤니티 이용가능
     - 작성자 본인만 게시글 및 댓글 수정 가능
     - 게시글 및 댓글 생성/수정 시각 정보 제공

     

## 3. 필수 기능

1. 관리자 뷰

- [x] 관리자 권한의 유저만 영화 등록 / 수정 / 삭제 권한을 가집니다.
- [x] 권리자 권한의 유저만 유저 관리 권한을 가집니다.
- [x] 장고에서 기본적으로 제공하는 admin 기능을 이용하여 구현합니다.
- [ ] Vue.js를 활용하는 경우에도 Django admin기능을 이용하여 구현할 수 있습니다.

2. 영화 정보

- [x] 영화 정보는 Database Seeding을 활용해 최소 50개 이상의 데이터가 존재하도록 구성해야 합니다.
- [x] 모든 로그인 된 유저는 영화에 대한 평점 등록 / 수정 / 삭제 등을 할 수 있어야 합니다.

3. 추천 알고리즘

- [x] 평점을 등록한 유저는 해당 정보를 기반으로 영화를 추천 받을 수 있어야 합니다.
- [x] 추천 알고리즘의 지정된 형식은 없으나, 사용자는 반드시 최소 1개 이상의 방식으로 영화를 추천 받을 수 있어야 합니다.
- [x] 추천 방식은 각 팀별로 자유롭게 선택할 수 있으며 어떠한 방식으로 추천 시스템을 구성 했는지 설명할 수 있어야 합니다.

4. 커뮤니티

- [x] 영화 정보와 관련된 대화를 할 수 있는 커뮤니티 기능을 구현해야 합니다.
- [x] 로그인한 사용자만 글을 조회 / 생성 할 수 있으며 작성자 본인만 글을 수정 / 삭제 할 수 있습니다.
- [x] 사용자는 작성된 게시글에 댓글을 작성할 수 있어야 하며 작성자 본인만 댓글을 삭제 할 수 있습니다.
- [x] 각 게시글 및 댓글은 생성 및 수정 시각 정보가 포함되어야 합니다.

5. 기타

- [x] 최소한 5개 이상의 URL 및 페이지를 구성해야 합니다.
- [ ] HTTP Method와 상태 코드는 상황에 맞게 적절하게 반환되어야 하며, 필요에따라 메시지 프레임워크 등을 사용하여 에러 페이지를 구성해야 합니다.
- [x] 필요한 경우 Ajax를 활용한 비동기 요청을 통해 사용자 경험을 적절하게 향상 시켜야 합니다.



---

## 5. 느낀점

최종 프로젝트를 진행하기전 정말 많은 기능들을 넣고 싶었고, 머릿속으로 구상했던 것들은 많았으나 프로젝트를 진행하면 진행 할 수록 알 수 없는 오류들과 만나고 그 오류를 해결하는데 시간이 많이 소요되었습니다. 그리고 초반 스케마를 짜고, 그대로 쭉 유지하면서 프로젝트를 진행하면 좋은데 중간중간에 시간적 제약과, 데이터를 가져오는데 많은 시간이 소모되고, 원하는대로 잘 진행이 되지않아 원했던 배급사의 최근 주식데이터 기반을 반영한 영화추천 알고리즘을 구현하지 못한것이 너무나 아쉽습니다. 

프로젝트를 진행하면 진행 할 수록 사용자에게 보여지는 프론트엔드도 중요하지만 Django로 진행하였던 백엔드의 모델링과 데이터가공, serializer가 튼튼해야지 내가 원하는 정보를 가져와 좀 더 많은 기능을 구현할 수 있다는 것을 깨닫고, 모델링에 대한 공부를 더 해봐야겠다는 생각을 하게 되었습니다. 뿐만 아니라 Vue로 front-end 개발을 진행하면서 처음 라이브강의 교수님이 한 말씀 중 많은데이터가 필요하지 않은곳에는 Vuex를 안쓰는 것이 더 현명하다고 하셔서 이번 프로젝트에는 사용을 하지 않았는데, 프로젝트를 진행하면서 많은시간을 데이터를 가져오고, 내가 원하는 형태로 가공하는데 시간이 매우매우 많이 걸려서 다음부터는 데이터를 편하게 관리 할 수 있는 Vuex를 제대로 공부하고, 다음 프로젝트에서 사용을 해야겠다는 생각을 하게 되었습니다. 

프로젝트를 진행하면서 커뮤니케이션의 중요성 또한 알게 되었고, 많이 부족해서 공부를 더 열심히 해야겠다는 생각이 들었습니다. 만족할만한 결과는 절대 아니지만, 많은 생각을 들게 해준 프로젝트였습니다. 더 열심히 공부해서 많은 프로젝트 경험을 쌓아가야겠다는 생각이 든 너무 소중한 경험이였습니다.

