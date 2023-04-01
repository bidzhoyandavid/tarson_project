from django.shortcuts import render, HttpResponse


# Create your views here.
def education(request):
    return render(request, 'education/educ.html')