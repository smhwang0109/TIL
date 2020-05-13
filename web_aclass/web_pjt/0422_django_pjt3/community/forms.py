from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    rank = forms.IntegerField(
        widget = forms.NumberInput(
            attrs={
                'min':'1',
                'max':'10',
            }
            )
        )
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'content', 'rank']

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'placeholder': '댓글을 작성해주세요.',
                'rows': 3,
            }
            )
        )
    class Meta:
        model = Comment
        fields = ['content']