from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# GenericViews (Auto):

# Create Category CRUD:
# Create & List of Category:

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Retrieve, Upate and Delete Category:

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    