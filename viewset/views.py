from rest_framework import viewsets
from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer


# Create your views here.

# Perform CRUD of Category using Viewset (AUTO)

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Perform CRUD of Product using Viewset (AUTO)

class ProducViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
