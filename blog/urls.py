from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.HomePageView.as_view(), name="home"),
    path(route="search/", view=views.PostSearchView.as_view(), name="search_post"),
    path(route="<slug:post>/", view=views.single_post, name="single_post"),
    path(route="tag/<slug:tag>/", view=views.TagListView.as_view(), name="post_by_tag"),
]
