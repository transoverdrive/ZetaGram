from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        view=views.Images.as_view(),
        name='images'
    ),
    path(
        "<int:image_id>/like/",
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
    path(
        "<int:image_id>/unlike/",
        view=views.UnLikeImage.as_view(),
        name='unlike_image'
    ),
    path(
        "<int:image_id>/comment/",
        view=views.CommentOnImage.as_view(),
        name='comment_image'
    ),
    path(
        "comment/<int:comment_id>/",
        view=views.Comment.as_view(),
        name='comment'
    ),
    path(
        "search/",
        view=views.Search.as_view(),
        name='search_tag'
    ),
    path(
        "<int:image_id>/comment/<int:comment_id>/",
        view=views.DeleteComment.as_view(),
        name='comment_delete'
    ),
    path(
        "<int:image_id>/",
        view=views.ImageDetail.as_view(),
        name='image_detail'
    ),
    

]