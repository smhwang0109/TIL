from django.shortcuts import render, redirect

from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'community/review_list.html', context)

def new(request):
    return render(request, 'community/new_review.html')

def create(request):
    pk = request.GET.get('pk')
    if int(pk):
        review = Review.objects.get(pk=pk)
    else:
        review = Review()
    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.rank = request.GET.get('rank')
    review.save()
    review_pk = review.pk
    return redirect(f'/community/review_detail/{review_pk}')

    

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review':review
    }
    return render(request, 'community/review_detail.html', context)

def edit(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review':review
    }
    return render(request, 'community/edit_review.html', context)

def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('/community/')