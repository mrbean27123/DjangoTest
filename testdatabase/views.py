from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.views.generic import DetailView, UpdateView, DeleteView


def testdatabase_main(request):
    movies = Movie.objects.order_by('rating')
    data = {
        "title": "Testdatabase page",
        "movies": movies,
    }
    return render(request, 'testdatabase/main.html', data)

def testdatabase_add_movie(request):
    error = ''
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testdatabase_main')
        else:
            error = form.errors
    movies = Movie.objects.order_by('-date_now')
    data = {
        "title": "add_movie page",
        "movies": movies,
        "movie_form": MovieForm(),
        "error": error,
    }
    return render(request, 'testdatabase/add_movie.html', data)

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'testdatabase/get_movie.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'get_movie page'
        return context

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'testdatabase/add_movie.html'
    form_class = MovieForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'update_movie page'
        context['movie_form'] = context['form']
        return context

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'testdatabase/delete_movie.html'
    success_url = '/testdatabase'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'delete_movie page'
        return context

