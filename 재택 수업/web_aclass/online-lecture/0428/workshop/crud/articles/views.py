from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Hashtag
from .forms import ArticleForm, HashtagForm
from django.contrib.auth.decorators import login_required


def index(request):
    articles = Article.objects.order_by('-pk')
    hashtag_form = HashtagForm()
    context = {
        'articles': articles,
        'hashtag_form': hashtag_form,
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)

@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')

@login_required
def add_hashtag(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    hashtags = Hashtag.objects.all()
    if request.user == article.user:
        if request.method == 'POST':
            hashtag_form = HashtagForm(request.POST)
            hashtag_content = request.POST.get('content')
            if hashtag_form.is_valid():
                for hashtag in hashtags:
                    if hashtag_content == hashtag.content:
                        if article not in hashtag.article.all():
                            hashtag.article.add(article)
                        break
                else:
                    hashtag = hashtag_form.save(commit=False)
                    hashtag.save()
                    hashtag.article.add(article)
    return redirect('articles:index')

@login_required
def delete_hashtag(request, article_pk, hashtag_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            hashtag = get_object_or_404(Hashtag, pk=hashtag_pk)
            hashtag.article.remove(article)
    return redirect('articles:index')
        