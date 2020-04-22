# 0421_Workshop

1. models.py

   ```python
   from django.db import models
   
   class Article(models.Model):
       title = models.CharField(max_length=100)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
   class Comment(models.Model):
       content = models.CharField(max_length=200)
       article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```
   
   
   
2. views.py

   ```python
   from django.shortcuts import render, redirect, get_object_or_404
   from .models import Article, Comment
   from .forms import ArticleForm, CommentForm
   from django.views.decorators.http import require_POST
   from django.contrib import messages
   
   def index(request):
       articles = Article.objects.all()
       context = {
           'articles': articles,
       }
       return render(request, 'articles/index.html', context)
   
   def create(request):
       if request.method == 'POST':
           form = ArticleForm(request.POST)
           if form.is_valid():
               article = form.save()
               return redirect('articles:detail', article.pk)
       else:
           form = ArticleForm()
       context = {
           'form': form,
       }
       return render(request, 'articles/form.html', context)
   
   def detail(request, article_pk):
       article = get_object_or_404(Article, pk=article_pk)
       comment_form = CommentForm()
       context = {
           'article': article,
           'comment_form': comment_form
       }
       return render(request, 'articles/detail.html', context)
   
   def comment_create(request, article_pk):
       article = get_object_or_404(Article, pk = article_pk)
       if request.method == 'POST':
           comment_form = CommentForm(request.POST)
           if comment_form.is_valid():
               comment = comment_form.save(commit=False)
               comment.article = article
               comment.save()
               messages.success(request, '댓글 작성이 완료되었습니다!')
           else:
               messages.warning(request, '댓글을 다시 입력해주세요!')
       return redirect('articles:detail', article_pk)
   
   @require_POST
   def comment_delete(request, article_pk, comment_pk):
       comment = get_object_or_404(Comment, pk = comment_pk)
       comment.delete()
       return redirect('articles:detail', article_pk)
   ```
   
   
   
3. forms.py

   ```python
   from django import forms
   from .models import Article, Comment
   
   class ArticleForm(forms.ModelForm):
       class Meta:
           model = Article
           fields = '__all__'
   
   class CommentForm(forms.ModelForm):
       class Meta:
           model = Comment
           fields = ['content']
   ```

