from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ItemListCreateView, ItemViewSet


# urlpatterns = [
#         path('items/', ItemListCreateView.as_view()),
# ]

router = DefaultRouter()
router.register('items', ItemViewSet)

urlpatterns = router.urls
