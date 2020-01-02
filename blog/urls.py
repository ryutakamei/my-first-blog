from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),    #サイトのデフォルトページをviews.pyのpost_listにリンク
    path('post/<int:pk>/', views.post_detail, name='post_detail') #記事のurlの作成
]
