from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import TweetForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout


# Create your views here.
def index(request):
    return render(request, "index.html")


def display_tweet_list(request):
    tweets = Tweet.objects.all().order_by("created_at")
    return render(request, "display_tweet_list.html", {"tweets": tweets})


@login_required
def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("display_tweet_list")
    else:
        form = TweetForm()

    return render(request, "tweet_form.html", {"form": form})


@login_required
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("display_tweet_list")
    else:
        form = TweetForm(instance=tweet)
        return render(request, "tweet_form.html", {"form": form})


def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("display_tweet_list")
    return render(request, "tweet_confirm_delete.html", {"tweet": tweet})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect("display_tweet_list")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})


def log_out(request):
    logout(request)
    return render(request, "registration/log_out.html")


def search_tweets(request):
    query = request.GET.get("q", "")  # Get the search query from the URL
    tweets = (
        Tweet.objects.filter(text__icontains=query).order_by("-created_at")
        if query
        else []
    )
    return render(
        request, "registration/search.html", {"tweets": tweets, "query": query}
    )
