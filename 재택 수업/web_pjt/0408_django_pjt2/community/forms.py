from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label='제목',
        help_text='100자 이내로 작성',
    )
    movie_title = forms.CharField(
        max_length=30,
        label='영화 제목',
        help_text='30자 이내로 작성',
    )
    rank = forms.IntegerField(
        label='평점',
        help_text='0~5점 사이로 작성',
        widget=forms.NumberInput(
            attrs={
                'min':0,
                'max':5,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder':'내용을 입력하세요.'
            }
        )
    )
    class Meta:
        model = Review
        fields = '__all__'