# 0421_Homework

1. Django에서 사용 가능한 lookup 세가지와 그 의미를 작성하시오.

   (1) `__gte` : 특정 숫자 이상에 해당하는 것들을 가져온다.
   
   (2) `__contains` : 특정 부분을 포함하는 것들을 가져온다.
   
   (2) `__startswith` : 시작하는 부분이 같은 것들을 가져온다.
   
   
   
   
   
2. 빈칸에 들어갈 수 있는 값 세 가지와 그 의미

   ```python
   class Comment(models.Model):
       content = models.CharField(max_length=100)
       article = modesl.ForeignKey(Article, on_delete=__(a)__)
   ```
   
   (1) `CASCADE` : 객체가 삭제되면 그 객체를 참조하고 있는 객체도 모두 삭제
   
   (2) `PROTECT ` : 객체를 참조하는 객체가 있으면 객체 삭제 불가
   
   (3) `SET_DEFAULT` : 객체가 삭제되면 그 객체를 참조하고 있는 객체들은 DEFAULT 값 참조
   
   
   
3. 빈칸에 들어갈 코드 작성

   ```python
   def comment_create(request, id):
       article = Article.objects.get(id=id)
       if request.method == "POST":
           form = CommentForm(request.POST)
           if form.is_valid():
               comment = form.save(__(a)__)
               comment.article = article
               comment.save()
               return redirect('articles:index')
   ```

   (a) : `commit=False`

4. 게시물 아래에 댓글을 출력하려고 한다. post와 comment 모델이 1:N으로 관계설정이 되어 있다고 가정 할 때 아래의 빈칸에 적절한 코드를 작성하시오.

   ```html
   <h1>{{ post.title}}</h1>
   {% for comment in __(a)__ %}
   	<p>{{ comment.content }}</p>
   {% empty %}
   	<p>댓글이 없습니다.</p>
   {% endfor %}
   ```

   (a) : post.comment_set.all
