# 0511_Workshop

![1_artist_list](C:\Users\user\house\web_aclass\online-lecture\0511\workshop\1_artist_list.JPG)

![2_artist_detail](C:\Users\user\house\web_aclass\online-lecture\0511\workshop\2_artist_detail.JPG)

![3_music_list](C:\Users\user\house\web_aclass\online-lecture\0511\workshop\3_music_list.JPG)

![4_music_detail](C:\Users\user\house\web_aclass\online-lecture\0511\workshop\4_music_detail.JPG)

![5_music_comments](C:\Users\user\house\web_aclass\online-lecture\0511\workshop\5_music_comments.JPG)

![6_comment_put](C:\Users\user\house\web_aclass\online-lecture\0511\workshop\6_comment_put.JPG)

![7_comment_delete](C:\Users\user\house\web_aclass\online-lecture\0511\workshop\7_comment_delete.JPG)



### views.py

```python
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseBadRequest
from .models import Artist, Music, Comment
from .serializers import ArtistSerializer, ArtistDetailSerializer, MusicSerializer, MusicDetailSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)

@api_view(['POST'])
def music_comments(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music=music)
        return Response(serializer.data)
    return HttpResponseBadRequest

@api_view(['GET', 'PUT', 'DELETE'])
def comment_put_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'성공적으로 수정되었습니다.', 'data':serializer.data})
        return HttpResponseBadRequest
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'message':'성공적으로 삭제되었습니다.'})
    return Response(serializer.data)


```



### serializers.py

```python
from rest_framework import serializers
from .models import Artist, Music, Comment

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class ArtistDetailSerializer(ArtistSerializer):
    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ['musics_count']

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content']

class MusicDetailSerializer(MusicSerializer):
    comments = CommentSerializer(many=True)

    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ['comments']
```

