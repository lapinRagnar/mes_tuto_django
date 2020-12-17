from django.db import models
from django.urls import reverse

# Create your models here.
class Artist(models.Model):
  name = models.CharField(max_length=200, unique=True)
  instrument = models.CharField(max_length=100, default='')
  
  def __str__(self):
    return self.name

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['id'] = id
      return context


class Contact(models.Model):
  email = models.EmailField(max_length=100)
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Album(models.Model):
  reference = models.IntegerField(null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  available = models.BooleanField(default=True)
  title = models.CharField(max_length=200)
  picture = models.URLField()
  artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

  def __str__(self):
    return self.title


class Booking(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  contacted = models.BooleanField(default=False)
  contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
  #album = models.OneToOneField(Album)
  album = models.OneToOneField(Album, on_delete=models.CASCADE, primary_key=True,)

  def __str__(self):
    return self.contact.name
