from django.views.generic import ListView, DetailView, View
from .models import Actor, Category, Movie
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
    if form.is_valid():
      form = form.save(commit=False)
      if request.POST.get("parent", None):
        form.parent_id = int(request.POST.get("parent"))
      form.movie = movie
      form.save()
    return redirect(movie.get_absolute_url())


class ActorView(DetailView):
  '''Вывод информации об актере'''
  model = Actor
  template_name = 'movies/actor.html'
  slug_field = "name"