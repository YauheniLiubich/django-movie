from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.models import Movie


class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = 'movies/movie_list.html'


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = 'url'
    # queryset = Movie.objects.get(url=slug)
    # template_name = 'movies/movie_detail.html'
    # def get(self, request, slug):
    #     movie =
    #     return render(request, , {'movie': movie})
