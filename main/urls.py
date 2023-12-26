from django.urls import path

from . import views

urlpatterns = [
    path('home-page',views.homepage, name = 'index'),
    path('question/<int:id>',views.questionPage, name = 'question' ),
    path('register/', views.registerpage, name = 'register'),
    path('login/',views.loginpage, name = 'login'),
    path('logout/',views.logoutPage, name = 'logout'),
    path('new-question',views.newQuestionPage, name= 'new-question'),
    path('about', views.about, name= 'aboutus'),
    path('profile/', views.profile, name= 'profile'),
    path('profile/edit', views.profile_edit, name= 'profile_edit'),
    path('delete_article/(?P<pk>\d+)', views.delete_article, name = 'delete_article'), # type: ignore
    path('user_quest', views.user_quest, name= 'user_quest'),
    
    path('', views.mainpage, name= 'main')
]