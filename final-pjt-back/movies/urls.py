from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),    
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_pk>/review/', views.review, name='review'),    
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_change, name='review_change'),    
    path('<int:movie_pk>/review/<int:review_pk>/check/', views.check_review, name='check_review'),    
    path('search/', views.search, name='search'),    
]
