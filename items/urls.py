from django.urls import path, include
from rest_framework.routers import DefaultRouter
from items.views import ItemViewSet, EstimateViewSet
#from items.views import ItemListCreateView, ItemRetrieveUpdateDeleteView

router = DefaultRouter()
router.register(r'', ItemViewSet, 'item-list')
router.register(r'', EstimateViewSet, 'estimate-list')

urlpatterns = [
    path('', include(router.urls)),
]
