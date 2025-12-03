from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# GenericViews (Auto):

# 1.Create Category CRUD:
    # Create & List of Category:

class CategoryListCreateView(generics.ListCreateAPIView):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    # Retrieve, Upate and Delete Category:

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# 2. Create CRUD of Product (AUTO):
    #  Create & List of Product:

class  ProductListCreateView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

   # Retrieve, Update and Delete/Destroy Product:

class ProuctDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
       