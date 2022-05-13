from django.views.generic import ListView, DetailView
from .models import Movie


# Create your views here.
class MovieView(ListView):
  '''Список Фильмов'''
  model = Movie
  queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
  '''Полное описание фильма'''
  model = Movie
  slug_field = "url"