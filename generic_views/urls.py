from .views import CategoryListCreateView, CategoryDetailView
from django.urls import path


urlpatterns = [

  path('categories/', CategoryListCreateView.as_view(), name='category-list'),
  path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

]