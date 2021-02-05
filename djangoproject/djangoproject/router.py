from rest_framework import routers
from product.api.viewset import UserViewSet, ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
