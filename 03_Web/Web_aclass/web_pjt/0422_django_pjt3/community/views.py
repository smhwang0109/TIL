from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-rank')
    context = {
        'reviews': reviews
    }
    return render(request, 'community/review_list.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
        else:
            messages.warning(request, '리뷰를 양식에 맞게 작성해주세요.')
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form
    }
    return render(request, 'community/form.html', context)

def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form
    }
    return render(request, 'community/review_detail.html', context)

@require_POST
@login_required
def delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
        return redirect('community:index')
    return redirect('community:detail', review.pk)

@login_required
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('community:detail', review.pk)
            else:
                messages.warning(request, '리뷰를 양식에 맞게 작성해주세요.')
        else:
            review_form = ReviewForm(instance=review)
        context = {
            'review_form':review_form
        }
        return render(request, 'community/form.html', context)
    else:
        return redirect('community:detail', review.pk)

@require_POST
@login_required
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
    return redirect('community:detail', review.pk)

@require_POST
@login_required
def comment_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('community:detail', review_pk)


