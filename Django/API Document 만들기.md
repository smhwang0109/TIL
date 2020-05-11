# API Document 만들기!



https://github.com/axnsan12/drf-yasg
https://drf-yasg.readthedocs.io/
https://drf-yasg.readthedocs.io/
https://drf-yasg.readthedocs.io/en/stable/readme.html#quickstart



### urls.py

```python
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# 설정
schema_view = get_schema_view(
   openapi.Info(
      title="Articles API",
      default_version='v1',
      description="게시판 API 서버입니다.",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
   ),
)

from django.urls import path
from . import views


# /api/v1/
# REST API의 URL
# C : POST /articles/
# R-index : GET /articles/
# R-detail : GET/article/<id>
# U : PUT /article/<id>
# D : DELETE /article/<id>

app_name='articles'

urlpatterns = [
    path('articles/', views.article_list_create),
    path('articles/<int:article_pk>/', views.article_detail_update_delete),
    path('comments/', views.comment_list),
    path('swagger/', schema_view.with_ui('swagger')),
    path('redocs/', schema_view.with_ui('redoc')),
]


```

