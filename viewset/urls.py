from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, ProducViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProducViewSet)

urlpatterns = [
    path("", include(router.urls))
]