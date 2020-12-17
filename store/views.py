from django.shortcuts import render

from store.models import Album, Artist, Booking, Contact

# Create your views here.
# Create your views here.
def index(request):
  artists = Artist.objects.all()
  return render(request, 'store/index.html', {'artists': artists})