"""
 All Imports request on the file
"""

from django.urls import path
from .views import (ArticleAPIView, ArticleRetrieveAPIView, 
                    RateAPIView, RateRetrieveAPIView )
from authors.apps.likedislike.views import LikeDislikeView
from authors.apps.likedislike.models import LikeDislike

from .models import Article
from .views import (
    ArticleAPIView,
    ArticleRetrieveAPIView,
    RateAPIView,
    RateRetrieveAPIView,
    TaggedItemRetrieveAPIView
)
app_name = 'articles'

urlpatterns = [
    path('', ArticleAPIView.as_view(), name='create_article'),
    path('<slug:slug>', ArticleRetrieveAPIView.as_view(), name="retrieve_article"),
    path('tags/all', TaggedItemRetrieveAPIView.as_view(), name="get_tags"),
    path('<slug:slug>/rate', RateAPIView.as_view(), name="create_get_rating"),
    path('rate/detail/<int:rate_id>', RateRetrieveAPIView.as_view(),
         name="get_update_delete_rating"),
    path('<slug:slug>/like/',
         LikeDislikeView.as_view(model=Article, vote_type=LikeDislike.LIKE),
         name='article_like'),
    path('<slug:slug>/dislike',
         LikeDislikeView.as_view(model=Article, vote_type=LikeDislike.DISLIKE),
         name='article_dislike'),
]
