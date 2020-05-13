from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review, Comment
from .forms import MovieForm, ReviewForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
def movie_create(request):
    if request.user.is_staff:
        if request.method == 'POST':
            movie_form = MovieForm(request.POST, request.FILES)
            if movie_form.is_valid():
                movie = movie_form.save()
                return redirect('movies:movie_detail', movie.pk)
        else:
            movie_form = MovieForm()
        context = {
            'form': movie_form
        }
        return render(request, 'movies/form.html', context)
    else:
        return redirect('movies:index')


def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews_aggregate = Review.objects.filter(movie=movie).aggregate(Avg('rank'))
    context = {
        'movie': movie,
        'review_rank': reviews_aggregate['rank__avg'],
    }
    return render(request, 'movies/movie_detail.html', context)

@login_required
def movie_update(request, movie_pk):
    if request.user.is_staff:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if request.method=='POST': # 관리자 권한이 있을 때만 수정 가능
            form = MovieForm(request.POST, request.FILES, instance=movie)
            if form.is_valid():
                movie = form.save(commit=False)
                movie.author=request.user
                movie.save()
                return redirect('movies:movie_detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
        context = {
            'form':form,
        }
        return render(request, 'movies/form.html', context)
    return redirect('movies:index')

@require_POST
@login_required
def movie_delete(request, movie_pk):
    if request.user.is_staff:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if request.user.is_staff:
            movie.delete()
    return redirect('movies:index')


@login_required
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = movie
            review.author = request.user
            review.save()
            return redirect('movies:review_detail', movie.pk, review.pk)
    else:
        review_form = ReviewForm()
    context = {
        'form': review_form
    }
    return render(request, 'movies/form.html', context)

def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
    }
    return render(request, 'movies/review_detail.html', context)


@login_required
def review_update(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.author:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.movie = movie
                review.author = request.user
                review.save()
                return redirect('movies:review_detail', movie.pk, review.pk)
        else:
            review_form = ReviewForm(instance=review)
        context = {
            'form':review_form
        }
        return render(request, 'movies/form.html', context)
    else:
        return redirect('movies:review_detail', movie.pk, review.pk)

@require_POST
@login_required
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.author:
        review.delete()
        return redirect('movies:movie_detail', movie_pk)
    return redirect('movies:review_detail', movie_pk, review.pk)

@require_POST
@login_required
def comment_create(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.review = review
        comment.save()
    return redirect('movies:review_detail', movie_pk, review.pk)

@login_required
def comment_update(request, movie_pk, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        if request.user == comment.author:
            comment_form = CommentForm(request.POST, instance=comment)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.review = review
                comment.save()
        return redirect('movies:review_detail', movie_pk, review.pk)
    else:
        comment_form = CommentForm(instance=comment)
    context = {
        'review': review,
        'comment_form': comment_form
    }
    return render(request, 'movies/review_detail.html', context)

@require_POST
@login_required
def comment_delete(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.author:
        comment.delete()
    return redirect('movies:review_detail', movie_pk, review_pk)

def review_like(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(id=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('movies:review_detail', movie_pk, review_pk)

def search(request):
    keyword = request.GET.get('keyword')
    movies = Movie.objects.filter(Q(title__icontains=keyword)|Q(summary__icontains=keyword)|Q(genre__icontains=keyword))
    context = {
        'movies': movies,
        'keyword': keyword,
    }
    return render(request, 'movies/index.html', context)