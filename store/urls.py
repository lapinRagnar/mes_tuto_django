from . import views
from django.urls import path

#app_name = 'blog'

urlpatterns = [
  path('store/', views.index, name="index_store"),


]