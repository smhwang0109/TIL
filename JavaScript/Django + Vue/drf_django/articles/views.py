from django.shortcuts import render, get_object_or_404
from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def index(request):
    # Article List
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleDetailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET'])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleListSerializer(article)
    return Response(serializer.data)