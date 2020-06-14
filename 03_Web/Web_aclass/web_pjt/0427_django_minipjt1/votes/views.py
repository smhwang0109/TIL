from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Vote, Choice1, Choice2, Comment
from .forms import VoteForm, ChoiceForm1, ChoiceForm2, CommentForm

# Create your views here.
def index(request):
    votes = Vote.objects.all()
    context = {
        'votes':votes,
    }
    return render(request, 'votes/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        vote_form = VoteForm(request.POST)
        choice_form1 = ChoiceForm1(request.POST)
        choice_form2 = ChoiceForm2(request.POST)
        if vote_form.is_valid():
            vote = vote_form.save(commit=False)
            vote.author = request.user
            vote.save()
            if choice_form1.is_valid():
                choice1 = choice_form1.save(commit=False)
                choice1.vote = vote
                if choice_form2.is_valid():
                    choice2 = choice_form2.save(commit=False)
                    choice2.vote = vote
                    choice1.save()
                    choice2.save()
                    return redirect('votes:detail', vote.pk)
    else:
        vote_form = VoteForm()
        choice_form1 = ChoiceForm1()
        choice_form2 = ChoiceForm2()
    context = {
        'vote_form' : vote_form,
        'choice_form1' : choice_form1,
        'choice_form2' : choice_form2,
    }
    return render(request, 'votes/create.html', context)

def detail(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    comment_form = CommentForm()
    choice1_response = vote.choice1.count
    choice2_response = vote.choice2.count
    if choice1_response+choice2_response != 0:
        choice1_rate = choice1_response/(choice1_response+choice2_response)*100
        choice2_rate = choice2_response/(choice1_response+choice2_response)*100
    else:
        choice1_rate = choice2_rate = 0
    context = {
        'vote': vote,
        'comment_form': comment_form,
        'choice1_rate': choice1_rate,
        'choice2_rate': choice2_rate,
    }
    return render(request, 'votes/detail.html', context)

@require_POST
def comment_create(request, vote_pk):
    if request.user.is_authenticated:
        vote = get_object_or_404(Vote, pk=vote_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.vote = vote
            comment.save()
            if comment.choice == '보기1':
                choice1 = vote.choice1
                choice1.count += 1
                choice1.save()
            else:
                choice2 = vote.choice2
                choice2.count += 1
                choice2.save()
        return redirect('votes:detail', vote.pk)
    else:
        return redirect('accounts:login')

def random(request):
    votes = Vote.objects.all()
    import random
    vote_pk = random.choice(votes).pk
    return redirect('votes:detail', vote_pk)