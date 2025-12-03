from .views import CategoryListCreateView, CategoryDetailView
from django.urls import path


urlpatterns = [

path('categories/', CategoryListCreateView.as_view()),
path('categories/', CategoryDetailView.as_view()),

]