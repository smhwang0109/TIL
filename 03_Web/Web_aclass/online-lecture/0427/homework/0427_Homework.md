# 0427_Homework

1. 다음 중 맞으면 T, 틀리면 F 를 작성하고 틀렸다면 이유를 함께 작성하시오

   - ForeignKey 는 부모 테이블의 데이터를 참조하기 위한 키이다.

     - True

   - 1:N 관계에서 1 은 N 의 데이터를 직접 참조 할 수 있다.

     - True (Comment_set과 같은 형태로 가능)

   - on_delete 속성은 ForeignKey 필드의 필수 인자이다.

     - True

   - 1:N 관계에서 ForeignKey 는 반드시 부모 테이블의 PrimaryKey 여야 한다.

     - True

       

2. 다음과 같이 이름이 articles 인 app 의 models.py 에 작성된 코드를 바탕으로 테이블이 만들어 졌을 때 , 데이터베이스에 저장되는 ForeignKey 컬럼의 이름과 테이블의 이름이 무엇인지 작성하시오.

![image-20200427175902565](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200427175902565.png)

ForeignKey 컬럼 : question_id

테이블 이름 : articles_question, aritcles_comment



3. 위 2 번 문제 모델 관계를 바탕으로 어느 template 페이지가 다음과 같이 작성되어 있을 때 , 질문(Question)에 작성된 모든 댓글(Comment)을 출력하고자 한다 . 해당 template 에서 Question 객체를 사용할 수 있다면 빈칸 (a)에 들어갈 알맞은 코드를 작성하시오

![image-20200427175933145](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200427175933145.png)

(a) : Question.comment_set.all



4. 다음과 같이 게시글을 삭제하는 delete 함수와 로그인을 위한 login 함수가 작성되어 있다  . 만약 비로그인 사용자가 삭제를 시도한다면 django 는 해당 사용자를 url 에 next 파라미터가 붙은 login 페이지로 redirect 한다 . (ex /accounts/login/?next=/articles/1/redirect 된 로그인 페이지에서 로그인에 성공했을 때 발생하는 HTTP response status code 를 작성하고 발생한 원인과 해결을 위해 코드를 수정하시오 . (게시글 삭제는 HTTP POST method 로만 가능하며 인증되지 않은 사용자는 메인페이지로 redirect 되어야 한다.)

![image-20200427180902468](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200427180902468.png)

![image-20200427180909197](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200427180909197.png)

HTTP response status code : 405

원인 : login_required에서 next 파라미터로 보낼 때는 GET 방식으로 보내기 때문에 require_POST의 조건에 맞지 않는다.

해결방법

```python
@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
    	article.delete()
    	return redirect('articles:index')
    else:
        return redirect('accounts:login')
```

