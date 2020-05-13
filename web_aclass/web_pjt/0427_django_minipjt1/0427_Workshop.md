# 0427_Workshop

1. accounts/urls.py

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'accounts'
   
   urlpatterns = [
       path('signup/', views.signup, name='signup'),
       path('login/', views.login, name='login'),
       path('logout/', views.logout, name='logout'),
   ]
   ```

   

2. accounts/views.py

   ```python
   from django.shortcuts import render, redirect
   from django.contrib.auth import authenticate
   from django.contrib.auth import login as auth_login
   from django.contrib.auth import logout as auth_logout
   from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
   from django.contrib.auth.decorators import login_required
   
   # Create your views here.
   def signup(request):
       if request.user.is_authenticated:
           return redirect('votes:index')
       if request.method == "POST":
           form = UserCreationForm(request.POST)
           if form.is_valid():
               new_user = form.save()
               authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
               auth_login(request, authenticated_user)
               return redirect(request.GET.get('next') or 'votes:index')
       else:
           form = UserCreationForm()
       context = {
           'form':form,
       }
       return render(request, 'accounts/form.html', context)
   
   def login(request):
       if request.user.is_authenticated:
           return redirect('votes:index')
       if request.method == "POST":
           form = AuthenticationForm(request, request.POST)
           if form.is_valid():
               auth_login(request, form.get_user())
               return redirect(request.GET.get('next') or 'votes:index')
       else:
           form = AuthenticationForm()
       context = {
           'form':form,
       }
       return render(request, 'accounts/form.html', context)
   
   @login_required
   def logout(request):
       auth_logout(request)
       return redirect('votes:index')
           
   ```

   

3. votes/models.py

   ```python
   from django.db import models
   from django.conf import settings
   
   # Create your models here.
   
   DEFAULT_USER_PK = 1
   
   class Vote(models.Model):
       author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=DEFAULT_USER_PK)
       question = models.CharField('질문', max_length=140)
       created_at = models.DateTimeField('투표 생성 시간', auto_now_add=True)
       is_active = models.BooleanField(default=True)
   
       def __str__(self):
           return f'{self.author}님의 질문 : {self.question}'
   
   class Choice1(models.Model):
       vote = models.OneToOneField(Vote, on_delete=models.CASCADE)
       choice_text1 = models.CharField('보기1 문항', max_length=140)
       count = models.IntegerField('보기1 투표수', default=0)
   
   class Choice2(models.Model):
       vote = models.OneToOneField(Vote, on_delete=models.CASCADE)
       choice_text2 = models.CharField('보기2 문항', max_length=140)
       count = models.IntegerField('보기2 투표수', default=0)
   
   class Comment(models.Model):
       author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=DEFAULT_USER_PK)
       vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
       CHOICE_SELECT = [
           ('보기1', '보기1'),
           ('보기2', '보기2')
       ]
       choice = models.CharField('선택', max_length=140, choices=CHOICE_SELECT)
       content = models.CharField('댓글', max_length=140)
       created_at = models.DateTimeField('댓글 생성 시간', auto_now_add=True)
       
   
   ```

   

4. votes/forms.py

   ```python
   from django import forms
   from .models import Vote, Choice1, Choice2, Comment
   
   class VoteForm(forms.ModelForm):
       class Meta:
           model = Vote
           exclude = ('author', 'created_at')
   
   class ChoiceForm1(forms.ModelForm):
       class Meta:
           model = Choice1
           exclude = ('vote', 'count')
   
   class ChoiceForm2(forms.ModelForm):
       class Meta:
           model = Choice2
           exclude = ('vote', 'count')
   
   class CommentForm(forms.ModelForm):
       class Meta:
           model = Comment
           exclude = ('author', 'vote', 'created_at')
   
   
   ```

   

5. votes/urls.py

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'votes'
   urlpatterns = [
       path('', views.index, name='index'),
       path('create/', views.create, name='create'),
       path('detail/<int:vote_pk>/', views.detail, name='detail'),
       path('<int:vote_pk>/comment_create/', views.comment_create, name='comment_create'),
       path('random/', views.random, name='random'),
   ]
   ```

   

6. votes/views.py

   ```python
   from django.shortcuts import render, redirect, get_object_or_404
   from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
   
   from .models import Vote, Choice1, Choice2, Comment
   from .forms import VoteForm, ChoiceForm1, ChoiceForm2, CommentForm
   
   # Create your views here.
   def index(request):
       votes = Vote.objects.all()
       context = {
           'votes':votes,
       }
       return render(request, 'votes/index.html', context)
   
   @login_required
   def create(request):
       if request.method == "POST":
           vote_form = VoteForm(request.POST)
           choice_form1 = ChoiceForm1(request.POST)
           choice_form2 = ChoiceForm2(request.POST)
           if vote_form.is_valid():
               vote = vote_form.save(commit=False)
               vote.author = request.user
               vote.save()
               if choice_form1.is_valid():
                   choice1 = choice_form1.save(commit=False)
                   choice1.vote = vote
                   if choice_form2.is_valid():
                       choice2 = choice_form2.save(commit=False)
                       choice2.vote = vote
                       choice1.save()
                       choice2.save()
                       return redirect('votes:detail', vote.pk)
       else:
           vote_form = VoteForm()
           choice_form1 = ChoiceForm1()
           choice_form2 = ChoiceForm2()
       context = {
           'vote_form' : vote_form,
           'choice_form1' : choice_form1,
           'choice_form2' : choice_form2,
       }
       return render(request, 'votes/create.html', context)
   
   def detail(request, vote_pk):
       vote = get_object_or_404(Vote, pk=vote_pk)
       comment_form = CommentForm()
       choice1_response = vote.choice1.count
       choice2_response = vote.choice2.count
       if choice1_response+choice2_response != 0:
           choice1_rate = choice1_response/(choice1_response+choice2_response)*100
           choice2_rate = choice2_response/(choice1_response+choice2_response)*100
       else:
           choice1_rate = choice2_rate = 0
       context = {
           'vote': vote,
           'comment_form': comment_form,
           'choice1_rate': choice1_rate,
           'choice2_rate': choice2_rate,
       }
       return render(request, 'votes/detail.html', context)
   
   @require_POST
   def comment_create(request, vote_pk):
       if request.user.is_authenticated:
           vote = get_object_or_404(Vote, pk=vote_pk)
           comment_form = CommentForm(request.POST)
           if comment_form.is_valid():
               comment = comment_form.save(commit=False)
               comment.author = request.user
               comment.vote = vote
               comment.save()
               if comment.choice == '보기1':
                   choice1 = vote.choice1
                   choice1.count += 1
                   choice1.save()
               else:
                   choice2 = vote.choice2
                   choice2.count += 1
                   choice2.save()
           return redirect('votes:detail', vote.pk)
       else:
           return redirect('accounts:login')
   
   def random(request):
       votes = Vote.objects.all()
       import random
       vote_pk = random.choice(votes).pk
       return redirect('votes:detail', vote_pk)
   ```
   
   