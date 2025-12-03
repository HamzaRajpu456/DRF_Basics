from .views import CategoryListCreateView, CategoryDetailView, ProductListCreateView, ProuctDetailView
from django.urls import path


urlpatterns = [

  path('categories/', CategoryListCreateView.as_view()),
  path('categories/<int:pk>/', CategoryDetailView.as_view()),
  
  
  path('products/', ProductListCreateView.as_view()),
  path('products/<int:pk>', ProuctDetailView.as_view()),

]