from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *


# Create your views here.
def education(request):
    query = request.GET.get("q")
    if query:
        education_list = EducationPost.objects.filter(title__icontains=query)
    else:
        education_list = EducationPost.objects.all()

    context = {"education_list": education_list}
    return render(request, "education/educ.html", context=context)


def vocabulary(request):
    context = {}
    return render(request, "education/vocabulary.html", context=context)


def vocabularyItem(request, voc_id):
    item = get_object_or_404(vocabulary, pk=voc_id)
    context = {"item": item}
    return render(request, "education/vocabularyitem.html", context=context)


def educationPost(request, educ_id):
    post = get_object_or_404(EducationPost, pk=educ_id)
    context = {"post": post}
    return render(request, "education/educpost.html", context=context)
