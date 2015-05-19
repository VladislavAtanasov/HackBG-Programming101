from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies, Projection

# Create your views here.
def index(request):
    movies = Movies.objects.all()
    projections = {}
    for movie in movies:
        projections[movie] = movie.projection_set.all()
    return render(request, "index.html", locals())
