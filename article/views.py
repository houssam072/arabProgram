from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import NewArticle
from .models import Article
from taggit.models import Tag
from django.template.defaultfilters import slugify


def add_article(request):
    post = NewArticle()
    if request.method == 'POST':
        try:
            post = NewArticle(request.POST)
            if post.is_valid():
                article = post.save(commit=False)
                article.auther = request.user
                article.save()
                # post.save_m2m()
                return redirect(reverse('approvedarticle_page'))
        except Exception as e:
            print(e)
            raise
    else:
        return render(request,'addarticle.html', {'post' : post})


def article_page(request):
    articles = Article.objects.filter(approved = True)
    context = {
        'articles':articles,
    }
    return render(request, 'article.html/',context)


def approved_article(request):
    article = Article.objects.filter(approved=False).order_by('-created_at')
    form = NewArticle()
    if request.user.is_superuser:
        if request.method == 'POST':
            form  = NewArticle(request.POST)
            id_list = request.POST.getlist('boxes')
            article.update(approved = False)
            for art in id_list:
                Article.objects.filter(pk = int(art)).update(approved=True)
                Article.objects.filter(pk = int(art)).update(message_body='تم نشر مقالتك بعنوان')
            return redirect('approved_article')
        
        return render(request,'approved_article.html',{'articles' : article})

    else:
        pass
    
def warn_message(request):
    user_articles = Article.objects.filter(approved = True)
    user_article = user_articles.filter(auther = request.user).filter(show = False)
    
    if request.method == 'POST':
            id_list = request.POST.getlist('boxes')
            user_article.update(show = False)
            for art in id_list:
                Article.objects.filter(pk = int(art)).update(show=True)
    return render(request,'warn.html',{'user_article' : user_article})


def approved_article_show(request, id):
    articles = Article.objects.filter(id = id)
    context = {
        'article' : articles
    }
    
    return render(request,'approved_article_show.html',context)


def approvedarticle_page(request):
    return render(request, 'approvedarticle_page.html')


def article_show(request, id):
    articles = Article.objects.filter(approved = True)
    article = articles.get(id = id)
    context = {
        'article' : article
    }
    
    return render(request,'article_show.html',context)


def user_article(request):
    user_articles = Article.objects.filter(approved = True)
    user_article = user_articles.filter(auther = request.user)
    return render(request,'user_article.html',{'user_article' : user_article})

