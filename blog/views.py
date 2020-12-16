from django.http.response import Http404
from django.shortcuts import render
from .mocks import Post
from django.http import Http404


# Create your views here.
def index(request):
  posts = Post.all()
  return render(request, 'blog/index.html', {'posts': posts})

def show(request, id):
  post = Post.find(id)
  try:
    return render(request, 'blog/show.html', {'post': post})
  except:
    raise Http404('Erreur 404, pas non trouvée!')
