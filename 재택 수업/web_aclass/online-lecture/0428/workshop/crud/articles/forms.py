from django import forms
from .models import Article, Hashtag


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article 
        exclude = ['created_at', 'updated_at', 'user', 'like_users']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['content',]