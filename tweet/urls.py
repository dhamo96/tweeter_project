from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(
        "", views.display_tweet_list, name="display_tweet_list"
    ),  # URL for the index view
    path("create/", views.create_tweet, name="create_tweet"),  # URL for the index view
    path(
        "<int:tweet_id>/edit/", views.edit_tweet, name="edit_tweet"
    ),  # URL for the index view
    path(
        "<int:tweet_id>/delete/", views.delete_tweet, name="delete_tweet"
    ),  # URL for the index view
    path("register/", views.register, name="register"),
    path("log_out/", views.log_out, name="log_out"),
    path("search/", views.search_tweets, name="search_tweets"),
]
