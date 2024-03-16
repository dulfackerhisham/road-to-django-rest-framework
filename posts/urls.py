from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("posts/", views.list_posts, name="list_post"),
    path("post/<int:post_id>/", views.detail_post, name="detail_post")
]

