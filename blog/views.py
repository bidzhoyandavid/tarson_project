from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *


# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, "blog/blog.html", context=context)


def blog_post(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    context = {"post": post}
    return render(request, "blog/blog_post.html", context=context)


def blog_search(request):
    query = request.GET.get("q")
    blog_list = Blog.objects.filter(title__icontains=query)
    context = {"blog_list": blog_list}
    return render(request, "blog/blog_search.html", context=context)
