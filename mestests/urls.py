from django.urls import path, include
import debug_toolbar
from . import views
from django.views.generic import TemplateView

urlpatterns = [
  #path('', TemplateView.as_view(template_name="index.html")),    
]
