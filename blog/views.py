from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from . import forms, models


class HomePageView(ListView):
    model = models.Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"


def single_post(request, post):
    post = get_object_or_404(models.Post, slug=post, status="published")
    posts = models.Post.objects.filter(author=post.author)[0:3]
    return render(
        request=request,
        template_name="blog/single.html",
        context={"post": post, "posts": posts},
    )


class TagListView(ListView):
    model = models.Post
    paginate_by = 10
    context_object_name = "tag_posts"
    slug_url_kwarg = "tag"
    query_pk_and_slug = True

    def get_queryset(self):
        return models.Post.objects.filter(tags__name__in=[self.kwargs["tag"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["tag"] = " ".join(self.kwargs["tag"].split("-"))
        context["tag"] = self.kwargs["tag"]
        return context

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/tag-list-elements.html"
        return "blog/tags.html"


class PostSearchView(ListView):
    model = models.Post
    context_object_name = "search_posts"
    paginate_by = 10
    form_class = forms.PostSearchForm

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/search-list-elements.html"
        return "blog/search.html"

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return models.Post.objects.filter(
                title__icontains=form.cleaned_data["search"]
            )
        return form.errors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get("search")

        return context
