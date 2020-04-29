# 0407_Exercise

![Read](C:\Users\user\house\web_aclass\online-lecture\0407\exercise\Read.PNG)

![Create](C:\Users\user\house\web_aclass\online-lecture\0407\exercise\Create.PNG)

![Detail](C:\Users\user\house\web_aclass\online-lecture\0407\exercise\Detail.PNG)

1. views.py

   ```python
   from django.shortcuts import render, redirect, get_object_or_404
   from .models import Article
   from .forms import ArticleForm
   
   # Create your views here.
   def index(request):
       articles = Article.objects.all()
       context = {
           'articles':articles
       }
       return render(request, 'articles/index.html', context)
   
   def create(request):
       if request.method == 'POST':
           form = ArticleForm(request.POST)
           if form.is_valid():
               article = form.save()
               return redirect('articles:index')
       else:
           form = ArticleForm()
       context = {
           'form':form
       }
       return render(request, 'articles/create.html', context)
   
   def detail(request, pk):
       article = get_object_or_404(Article, pk=pk)
       context = {
           'article':article
       }
       return render(request, 'articles/detail.html', context)
   
   ```

   

2. forms.py

   ```python
   from django import forms
   from .models import Article
   
   class ArticleForm(forms.ModelForm):
       class Meta:
           model = Article
           fields = ['title', 'content']
   ```

   