from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

# Create your views here.
# Generic View : we can also crete individually or in group:

# CREATE & LIST view
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Update, Retreive, Delete view:

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# ViewSets of (ITEM): 


class ItemViewSet(viewsets.ViewSet):

    def list(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        items = Item.objects.get(pk=pk)
        serializer = ItemSerializer(items)
        return Response(serializer.data)



# ModelViewSets :
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer