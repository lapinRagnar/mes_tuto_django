from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('blog/', views.index, name="blog"),
    path('blog/post/<int:id>', views.show, name="blog"),

]