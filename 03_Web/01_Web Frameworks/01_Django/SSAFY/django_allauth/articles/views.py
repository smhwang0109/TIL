from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Article

def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'articles': articles,
        'page_obj': page_obj,
    }
    return render(request, 'articles/article_list.html', context)
