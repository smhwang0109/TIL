# 06 pk, path converter, get_object_or_404

## 글자 수 제한

```python
# models.py에 class 안에
    def summary(self):
        return self.body[:100]
```

home.html 수정

```python
# 수정 전
{% for blog in blogs.all %}
    <h1>{{blog.title}}</h1>
    <p>{{blog.pub_date}}</p>
    <p>{{blog.body}}</p>
    <br>
    <br>
{% endfor %}

# 수정 후 
{% for blog in blogs.all %}
    <h1>{{blog.title}}</h1>
    <p>{{blog.pub_date}}</p>
    <p>{{blog.summary}}</p>
    <br>
    <br>
{% endfor %}
```



## more 링크 클릭했을 때 detail.html 페이지 내보내기

detail.html 은 100글자로 요약한 내용이 아닌, 전체 내용을 담고 있어야 합니다.

그럼 각 글마다 각각에 해당되는 detail.html 을 만들어주어야 할까요?

그러면 글이 많아질 경우, 수없는 detail.html이 필요할 겁니다.

따라서 하나의 detail.html 만들고 상황에 맞게 내용을 넣어주도록 하겠습니다.

좀 더 자세히 설명을 하자면,

우리는 각 상황에 몇 번째 블로그 객체를 호출하는지를 알아야하고, **(pk)**

그 상황에 맞는 url 은 .../blog/{객체번호} 처럼 객체에 따라서 달라야 할 것입니다. **(path converter)**

또한 없는 객체 번호를 호출할 경우에는 에러 페이지를 호출해야 합니다. **(get_object_or_404)**



에러 내용을 살펴보면 `post_detail` 뷰가 `pk` 라고 하는 예상치 못한 키워드 인자를 받았다고 한다. 즉, `views.py` 의 `post_detail` 함수는 키워드 인자를 받지 않는데 `pk` 라는 키워드 인자가 전달되었다는 말이다.
사용자가 예를들어 `post/1` 의 주소에 접속하면 `r'^post/(?P\d+)/'` 와 매칭되고 `post_detail` 함수에 `request` 가 전달되어 실행된다. 그런데 여기서 숫자 `1` 이 `pk` 라는 이름의 그룹에 저장되어 있는데 이럴 경우에는 `post_detail` 함수에 `request` 와 함께 `pk=1` 이라는 키워드 인자가 전달된다. `post_detail` 함수는 `request` 만 받도록 되어 있으므로 에러가 나는 것이다.
이를 해결하기 위해서 아래와 같이 `post_detail` 함수가 `pk` 라는 키워드 인자를 받도록 해주자.

1. detail 함수 정의

```python
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})
```

2. detail.html 정의

```html
    <h1>{{blog.title}}</h1>
    <p>{{blog.pub_date}}</p>
    <p>{{blog.body}}</p>
    <br>
    <br>
```

3. home.html 에서 링크 설정

```html
	<p>{{blog.summary}}<a href="/blog/{{blog.id}}">...more</a></p>
```

4. url 설계

```python
# urls.py에 urlpatterns에 추가
	path('blog/<int:blog_id>', blog.views.detail, name='detail'),
```

*** pathconverter**

\<int:blog_id> 는 기존 str 타입의 id를 int로 바꿔준다.

