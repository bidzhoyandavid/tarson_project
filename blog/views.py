from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from taggit.models import Tag
from django.db.models import Count


# Create your views here.
def blog(request, tag_slug=None):
    query = request.GET.get("q")
    if query:
        tag = None
        blogs = Blog.objects.filter(title__icontains=query)
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            blogs = Blog.objects.filter(tags__in=[tag])
    else:
        tag = None
        blogs = Blog.objects.all()
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            blogs = Blog.objects.filter(tags__in=[tag])
    context = {"blogs": blogs, "tag": tag}
    return render(request, "blog/blog.html", context=context)


def blog_post(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)

    post_tags_id = Blog.objects.values_list("id", flat=True)
    similar_posts = Blog.objects.filter(tags__in=post_tags_id).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-date_created"
    )[:3]

    context = {"post": post, "similar_posts": similar_posts}
    return render(request, "blog/blog_post.html", context=context)
