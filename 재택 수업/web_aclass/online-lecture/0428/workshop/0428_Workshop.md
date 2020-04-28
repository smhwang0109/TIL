# 0428_Exercise

![팔로워](C:\Users\user\house\web_aclass\online-lecture\0428\workshop\팔로워.PNG)

![팔로잉](C:\Users\user\house\web_aclass\online-lecture\0428\workshop\팔로잉.PNG)

1. accounts/views.py

   ```python
   from django.shortcuts import render, redirect, get_object_or_404
   from django.contrib.auth.forms import AuthenticationForm
   from .forms import CustomUserCreationForm
   from django.contrib.auth.decorators import login_required
   from django.contrib.auth import login as auth_login, logout as auth_logout
   from django.contrib.auth import get_user_model
   
   User = get_user_model()
   
   
   def signup(request):
       if request.method == 'POST':
           form = CustomUserCreationForm(request.POST)
           if form.is_valid():
               user = form.save()
               auth_login(request, user)
               return redirect('articles:index')
       else:
           form = CustomUserCreationForm()
       context = {
           'form': form,
       }
       return render(request, 'accounts/signup.html', context)
   
   def login(request):
       if request.method == 'POST':
           form = AuthenticationForm(request, request.POST)
           if form.is_valid():
               auth_login(request, form.get_user())
               return redirect('articles:index')
       else:
           form = AuthenticationForm()
       context = {
           'form': form,
       }
       return render(request, 'accounts/login.html', context)
   
   @login_required
   def logout(request):
       auth_logout(request)
       return redirect('articles:index')
   
   @login_required
   def follow(request, username):
       person = get_object_or_404(User, username=username)
       user = request.user
       if user in person.followers.all():
           person.followers.remove(user)
       else:
           person.followers.add(user)
       return redirect('profile', person.username)
   
   @login_required
   def profile(request, username):
       person = get_object_or_404(User, username=username)
       context = {
           'person':person,
       }
       return render(request, 'accounts/profile.html', context)
   ```

   

2. accounts/models.py

   ```python
   from django.db import models
   from django.contrib.auth.models import AbstractUser
   from django.conf import settings
   
   class User(AbstractUser):
       followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
   
   ```
   
   
   
3. profile.html

   ```python
   {% extends 'base.html' %}
   
   {% block content %}
   <h1>{{ person.username }}님의 프로필</h1>
   <p>팔로워 : {{ person.followers.count }}명</p>
   <ul>
     {% for follower in person.followers.all %}
     <li>{{ follower.username }}</li>
     {% endfor %}
   </ul>
   <p>팔로잉 : {{ person.followings.count }}명</p>
   <ul>
     {% for following in person.followings.all %}
     <li>{{ following.username }}</li>
     {% endfor %}
   </ul>
   {% if request.user != person %}
     {% if request.user in person.followers %}
     <a href="{% url 'follow' person.username %}">언팔로우</a>
     {% else %}
     <a href="{% url 'follow' person.username %}">팔로우</a>
     {% endif %}
   {% endif %}
   <h2>{{ person.username }}님이 작성한 글 : {{ person.article_set.count }}개</h2>
   <hr>
   {% for article in person.article_set.all %}
     <p>제목 : {{ article.title }}</p>
     <p>내용 : {{ article.content }}</p>
     {% include 'articles/like.html' %}
     <hr>
   {% endfor %}
   {% endblock %}
   ```

   

4. like.html

   ```python
   <p>{{ article.like_users.count }}명이 좋아합니다.</p>
   {% if request.user in article.like_users.all %}
   <a href="{% url 'articles:like' article.pk %}">
     <i class="fas fa-heart" style="color: red;"></i>
   </a>
   {% else %}
   <a href="{% url 'articles:like' article.pk %}">
     <i class="far fa-heart" style="color: black;"></i>
   </a>
   {% endif %}
   ```

   