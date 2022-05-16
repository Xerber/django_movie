from django.views.generic import ListView, DetailView, View
from .models import Movie
from django.shortcuts import redirect
from .forms import ReviewForm

# Create your views here.
class MovieView(ListView):
  '''Список Фильмов'''
  model = Movie
  queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
  '''Полное описание фильма'''
  model = Movie
  slug_field = "url"

class AddReview(View):
  '''Отзывы'''
  def post(self,request,pk):
    form = ReviewForm(request.POST)
    movie = Movie.objects.get(id=pk)
    if form.is_valid:
      form = form.save(commit=False)
      form.movie = movie
      form.save()
    return redirect(movie.get_absolute_url())