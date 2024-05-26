from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from mypystarter.auth.authentication import JWTTokenObtainPairView
from tenant.views import ProductView, CityView

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'products', ProductView, basename='product')
router.register(r'cities', CityView, basename='city')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', JWTTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
