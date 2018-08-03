from django.urls import path
from . import views

urlpatterns = [
    path(
        "all/",
        view=views.ListAllImages.as_view(),
        name='all_images'
    ),

    path(
        "comments/",
        view=views.ListAllComments.as_view(),
        name='comments'
    ),

    path(
        "likes/",
        view=views.ListAllLikes.as_view(),
        name='likes'
    )
]
