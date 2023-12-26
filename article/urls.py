from django.urls import path

from . import views

urlpatterns = [
    path('add_article/',views.add_article, name = 'add_article'),
    path('approved_article/',views.approved_article, name = 'approved_article'),
    path('approvedarticle_page/',views.approvedarticle_page, name = 'approvedarticle_page'),
    path('article_page/',views.article_page, name = 'article_page'),
    path('user_article/',views.user_article, name = 'user_article'),
    path('article_show/<int:id>',views.article_show, name = 'article_show'),
    path('approved_article_show/<int:id>',views.approved_article_show, name = 'approved_article_show'),
    path('approved_article',views.approved_article, name = 'approved_article'),
    path('warn_message',views.warn_message, name = 'warn_message'),
    path('tag/<slug:tag_slug>',views.article_page, name = 'tag'),
]