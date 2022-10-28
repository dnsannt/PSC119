from spgdt.models import Pbfree, Telp, Giat
from spgdt.serializers import PbfreeSerializer, SpgdtSerializer, GiatSerializer
from rest_framework import viewsets, permissions


class PbfreeViewset(viewsets.ModelViewSet):
    queryset = Pbfree.objects.all()
    serializer_class = PbfreeSerializer
    # permission dengan django admin harus login dulu
    permission_classes = [permissions.IsAuthenticated]


class SpgdtViewset(viewsets.ModelViewSet):
    queryset = Telp.objects.all()
    serializer_class = SpgdtSerializer
    # permission api django admin harus login dulu
    permission_classes = [permissions.IsAuthenticated]


class GiatViewset(viewsets.ModelViewSet):
    queryset = Giat.objects.all()
    serializer_class = GiatSerializer
    # permission api django admin harus login dulu
    permission_classes = [permissions.IsAuthenticated]
