from django.urls import path
from .views import ProductListCreateAPI,ProductDetailAPI


urlpatterns = [

    path("products/", ProductListCreateAPI.as_view()),
    path("products/<int:id>/",ProductDetailAPI.as_view())
]