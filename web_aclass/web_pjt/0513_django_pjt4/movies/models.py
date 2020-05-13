from django.db import models
from django.conf import settings

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField()
    distributor = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    leading_actor = models.CharField(max_length=100)
    release_date = models.DateField()
    GENRE_CHOICES = [
        ('SF', 'SF'),
        ('멜로', '멜로'),
        ('액션', '액션'),
        ('코미디', '코미디'),
        ('스릴러', '스릴러'),
        ('음악/뮤지컬', '음악/뮤지컬'),
        ('판타지', '판타지')
    ]
    genre = models.CharField(max_length=7, choices=GENRE_CHOICES)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_reviews')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)