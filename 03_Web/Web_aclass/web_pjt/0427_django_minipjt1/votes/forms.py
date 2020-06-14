from django import forms
from .models import Vote, Choice1, Choice2, Comment

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        exclude = ('author', 'created_at')

class ChoiceForm1(forms.ModelForm):
    class Meta:
        model = Choice1
        exclude = ('vote', 'count')

class ChoiceForm2(forms.ModelForm):
    class Meta:
        model = Choice2
        exclude = ('vote', 'count')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('author', 'vote', 'created_at')

