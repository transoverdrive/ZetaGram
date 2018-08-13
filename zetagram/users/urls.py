from django.urls import path
from . import views

urlpatterns = [
    path(
        "explore/",
        view=views.ExploreUsers.as_view(),
        name='explore_users'
    ),
    path(
        "<int:user_id>/follow/",
        view=views.FollowUser.as_view(),
        name='follow_users'
    ),
    path(
        "<int:user_id>/unfollow/",
        view=views.UnFollowUser.as_view(),
        name='unfollow_users'
    ),
    path(
        "<str:username>/followers/",
        view=views.UserFollowers.as_view(),
        name='user_followers'
    ),
    path(
        "search/",
        view=views.Search.as_view(),
        name='search_user'
    ),
    path(
        "<str:username>/",
        view=views.UserProfile.as_view(),
        name='user_profile'
    ),
    path(
        "<str:username>/password/",
        view=views.ChangePassword.as_view(),
        name='change_password'
    ),
    path(
        "login/facebook/",
        view=views.FacebookLogin.as_view(),
        name='facebook_login'
    )
]


