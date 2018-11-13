from django.urls import path

from .views import (ArticlesListCreateAPIView,
                    GetArticleBySlugApiView, RetrieveUpdateArticleByIdApiView,
                    RateCreateAPIView, RateRetrieveAPIView,)

urlpatterns = [
    path('', ArticlesListCreateAPIView.as_view(),
         name='list_create_articles'),
    path('<int:pk>', RetrieveUpdateArticleByIdApiView.as_view(),
         name='get_article_byId'),
    path('<slug:slug>', GetArticleBySlugApiView.as_view(),
         name='get_article_bySlug'),
    path('add_rates/<slug>', RateCreateAPIView.as_view(),
         name='add_article_ratings'),
    path('view_rates/<slug>', RateRetrieveAPIView.as_view(),
         name='view_average_article_ratings'),
]
