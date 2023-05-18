from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from taggit.models import Tag
from django.db.models import Count


# Create your views here.
def vocabulary(request):
    query = request.GET.get("q")
    if query:
        vocabulary_list = Vocabulary.objects.filter(title__icontains=query)
    else:
        vocabulary_list = Vocabulary.objects.all()
    context = {"vocabulary_list": vocabulary_list}
    return render(request, "education/vocabulary.html", context=context)


def vocabularyItem(request, voc_id):
    item = get_object_or_404(Vocabulary, pk=voc_id)
    context = {"item": item}
    return render(request, "education/vocabularyitem.html", context=context)


def education(request, tag_slug=None):
    query = request.GET.get("q")
    if query:
        tag = None
        education_list = EducationPost.objects.filter(title__icontains=query)
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            education_list = EducationPost.objects.filter(tags__in=[tag])
    else:
        tag = None
        education_list = EducationPost.objects.all()
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            education_list = EducationPost.objects.filter(tags__in=[tag])

    context = {"education_list": education_list, "tag": tag}
    return render(request, "education/educ.html", context=context)


def educationPost(request, educ_id):
    post = get_object_or_404(EducationPost, pk=educ_id)

    post_tags_id = EducationPost.tags.values_list("id", flat=True)
    similar_posts = EducationPost.objects.filter(tags__in=post_tags_id).exclude(
        id=post.id
    )
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-date_upload"
    )[:3]

    context = {"post": post, "similar_posts": similar_posts}
    return render(request, "education/educpost.html", context=context)
