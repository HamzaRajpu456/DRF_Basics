from django.urls import path
from .views import ProductListCreateAPI,ProductDetailAPI


url_pattern = [

    path("products/", ProductListCreateAPI.as_view()),
    path("products/<int:id>/",ProductDetailAPI.as_view())

]