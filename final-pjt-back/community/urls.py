from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),    
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/check/<str:username>/', views.check_article, name='check_article'),
    path('<int:article_pk>/comment/', views.comment, name='comment'),    
    path('<int:article_pk>/comment/<int:comment_pk>/', views.comment_change, name='comment_change'),    
    path('<int:article_pk>/comment/<int:comment_pk>/check/<str:username>/', views.check_comment, name='check_comment'),    
]
