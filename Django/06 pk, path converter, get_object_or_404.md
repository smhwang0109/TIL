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

1. detail 함수 정의





2. url 설계

```python
# urls.py에 urlpatterns에 추가
	path('blog/<int:blog_id>', blog.views.detail, name='detail'),
```

*** pathconverter**

\<int:blog_id> 는 기존 str 타입의 id를 int로 바꿔준다.

