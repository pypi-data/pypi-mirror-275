from rest_framework_simplejwt.views import TokenObtainPairView

from core.auth.serializers import AuthSerializer


class JWTTokenObtainPairView(TokenObtainPairView):
    serializer_class = AuthSerializer
