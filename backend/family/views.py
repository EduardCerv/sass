from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Family
from .serializers import FamiliSerializer


class FamilyViewSet(ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamiliSerializer
    permission_classes = [AllowAny]