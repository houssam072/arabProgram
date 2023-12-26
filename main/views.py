from logging import exception
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import LoginUserForms, NewQuestionForm, NewResponseForm, RegisterUserForms, ProfileForm, UserForm
from .models import Question,Profile
from django.apps import apps
from django.contrib import messages
from .temp_final_end import nlp





# Create your views here.
def mainpage(request):
    try:
        model_article = apps.get_model('article','Article')
        article_not_approved = model_article.objects.all().filter(approved = False)
        article_approved = model_article.objects.all().filter(approved = True).filter(auther = request.user).filter(show = False)
        if request.user.is_superuser:
            if article_not_approved.exists():
                messages.info(request,'هناك مقالة تحتاج الى مراجعة !' ,extra_tags='review')
            return render(request, 'mainpage.html') 
        else:
            if article_approved.exists():
                messages.info(request,'هناك ملاحظات تحتاج الى مراجعة !' ,extra_tags='review')
            return render(request, 'mainpage.html')
    except:
            return render(request, 'mainpage.html')


def delete_article(request, pk):  
    model_article = apps.get_model('article','Article')
    if request.user.is_superuser:
        model_article.objects.get(pk = pk).delete()
        return redirect('approved_article')
    
def registerpage(request):
    form = RegisterUserForms()
    if request.method == 'POST':
        try:
            form = RegisterUserForms(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('profile_edit')
        except Exception as e:
            print(e)
            raise
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def loginpage(request):
    form = LoginUserForms()
    if request.method == 'POST':
        try:
            form = LoginUserForms(data = request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request,user)
                return redirect('/')
        except Exception as e:
            print(e)
            raise
    context = {
        'form':form
    }
    return render(request, 'login.html', context)

@login_required(login_url='register')
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='register') # type: ignore
def newQuestionPage(request):
    form  = NewQuestionForm()
    if request.method == 'POST':
        try:
            form  = NewQuestionForm(request.POST, request.FILES)
            if form.is_valid():
                quest_title = request.POST.get('title')
                quest_body = request.POST.get('body')
                title_before_nlp = nlp(quest_title)
                body_before_nlp = nlp(quest_body)
                print(title_before_nlp)
                print(body_before_nlp)
                question = form.save(commit= False)
                form.cleaned_data['title']
                form.cleaned_data['body']
                question.title = title_before_nlp
                question.body = body_before_nlp
                question.auther = request.user
                question.save()
                return redirect('index')
                
        except Exception as e:
            print(e)
            raise
    else:
        context = {
            'form' : form
        }
        return render(request,'new-question.html',context)

def homepage(request):
    questions = Question.objects.all().order_by('-created_at')
    context = {
        'questions' : questions
    }
    return render(request,'homepage.html',context)



def questionPage(request, id):
    form = NewResponseForm()
    if request.method == 'POST':
        try:
            form = NewResponseForm(request.POST)
            if form.is_valid():
                res_body = request.POST.get('body')
                res_after_nlp = nlp(res_body)
                print(res_after_nlp)
                response = form.save(commit= False)
                form.cleaned_data['body']
                response.body = res_after_nlp
                response.user = request.user
                response.question = Question(id = id)
                response.save()
                return redirect('/question/'+str(id)+'#'+str(response.id))


        except exception as e:
            print(e)
            raise
        

    question = Question.objects.get(id = id )
    context = {
        'question' : question,
        'responce_form':form
    }
    return render(request,'question.html',context)

def about(requst):
    return render(requst, 'aboutUs.html')

def user_quest(request):
    user_quest = Question.objects.filter(auther = request.user)
    return render(request,'user_quest.html',{'user_quest' : user_quest})

def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render(request,'profile.html',{'profile' : profile})
    
def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)

        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    
    return render(request,'profile_edit.html',{'userform' : userform, 'profileform' : profileform})
    


