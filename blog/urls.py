from django.urls import path
from . import views

from .views import CategoryNew, CategoryList

# from .views import PostDetail, PostList

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("drafts/", views.post_draft_list, name="post_draft_list"),
    path("post/<pk>/publish/", views.post_publish, name="post_publish"),
    path("post/<pk>/remove", views.post_remove, name="post_remove"),
    path("category/new", CategoryNew.as_view(), name="category_new"),
    path("category/", CategoryList.as_view(), name="category_list"),
    path("category/<str:cats>", views.category_detail, name="category_detail"),
    # path("", PostList.as_view(), name="post_list"),
    # path("post/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    # path("post/new", PostNew.as_view(), name="post_new"),
    # path("post/<int:pk>/edit/", PostEdit.as_view(), name="post_edit"),
    # path("post/<pk>/remove", PostRemove.as_view(), name="post_remove"),
]
