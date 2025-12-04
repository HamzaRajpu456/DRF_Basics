from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

# Perfrom CRUD Manually :



class ProductListCreateAPI(APIView):

    def get(self, request):
       
        product = Product.objects.all()
        serializer = ProductSerializer(product, many = True) 
        return Response (serializer.data)
        
    def post(self, request):
        
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    



class ProductDetailAPI(APIView):

    def get_object(self, id):
        try:
            return Product.objects.get(id = id)
        except Product.DoesNotExist:
            return None
        
    def get(self, request, id):
        product = self.get_object(id)
        if not product:
            return Response({"Error":"Not Found"})
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    

    def put(self,request,id):
        product = self.get_object(id)
        if not product:
            return Response({"Error":"Product not Found!"})
        
        serializer = ProductSerializer(product, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,id):
        product = self.get_object(id)
        
        if not product:
            return Response({"error":"Product not found!"})
        
        product.delete()
        return Response({"Message":"Product Deleted Successfully"})
    