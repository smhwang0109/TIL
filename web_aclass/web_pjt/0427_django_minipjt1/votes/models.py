from django.db import models
from django.conf import settings

# Create your models here.

DEFAULT_USER_PK = 1

class Vote(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=DEFAULT_USER_PK)
    question = models.CharField('질문', max_length=140)
    created_at = models.DateTimeField('투표 생성 시간', auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.author}님의 질문 : {self.question}'

class Choice1(models.Model):
    vote = models.OneToOneField(Vote, on_delete=models.CASCADE)
    choice_text1 = models.CharField('보기1 문항', max_length=140)
    count = models.IntegerField('보기1 투표수', default=0)

class Choice2(models.Model):
    vote = models.OneToOneField(Vote, on_delete=models.CASCADE)
    choice_text2 = models.CharField('보기2 문항', max_length=140)
    count = models.IntegerField('보기2 투표수', default=0)

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=DEFAULT_USER_PK)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    CHOICE_SELECT = [
        ('보기1', '보기1'),
        ('보기2', '보기2')
    ]
    choice = models.CharField('선택', max_length=140, choices=CHOICE_SELECT)
    content = models.CharField('댓글', max_length=140)
    created_at = models.DateTimeField('댓글 생성 시간', auto_now_add=True)
    
