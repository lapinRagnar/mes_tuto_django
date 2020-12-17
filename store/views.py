from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from store.models import Album, Artist, Booking, Contact

from django.urls import reverse_lazy


# Create your views here.
# Create your views here.
#def index(request):
#  artists = Artist.objects.all()
#  return render(request, 'store/index.html', {'artists': artists})

# gestion d'artiste

class IndexView(ListView):
  model = Artist
  template_name = 'store/artists/index.html'
  context_object_name = 'artists'

  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    artists = self.get_queryset()
    page = self.request.GET.get('page')

    context['artists'] = artists
    return context

class ArtistCreateView(CreateView):
  model = Artist
  template_name = 'store/artists/create.html'
  fields = ('name', 'instrument', )
  success_url = reverse_lazy('index_artist')

class ArtistDetailView(DetailView):

  model = Artist
  template_name = 'store/artists/show.html'
  context_object_name = 'artist'

class ArtistUpdateView(UpdateView):

    model = Artist
    template_name = 'store/artists/update.html'
    context_object_name = 'artist'
    fields = ('name', 'instrument',)

    def get_success_url(self):
      return reverse_lazy('show_artist', kwargs={'pk': self.object.id})

class ArtistDeleteView(DeleteView):
  model = Artist
  template_name = 'store/artists/delete.html'
  def get_success_url(self):
    return reverse_lazy('index_artist', kwargs={'pk': self.object.id})


# gestion de contact




