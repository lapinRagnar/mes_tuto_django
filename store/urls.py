from . import views
from django.urls import path
from store.views import IndexView

#app_name = 'blog'

urlpatterns = [
  #path('store/', views.index, name="index_store"),

  #gestion d'Artiste

  path('', IndexView.as_view(), name='index_artist'),
  path('create/', views.ArtistCreateView.as_view(), name='create_artist'),
  path('<int:pk>/', views.ArtistDetailView.as_view(), name='show_artist'),
  path('<int:pk>/update', views.ArtistUpdateView.as_view(), name='update_artist'),
  path('<int:pk>/delete', views.ArtistDeleteView.as_view(), name='delete_artist'),
  #path('<pk>/', StoreDetailView.as_view(), name='show_store'),

  # gestion de contact



]