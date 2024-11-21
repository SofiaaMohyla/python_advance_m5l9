from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin, \
    CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Artifact, Anomaly
from .serializers import ArtifactSerializer, AnomalySerializer


class ArtifactViewSet(ModelViewSet):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer


class AnomalyViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    #UpdateModelMixin,
    #DestroyModelMixin,
    GenericViewSet
):
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer


class AnomalyListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AnomalyRetrieveView(GenericAPIView, RetrieveModelMixin):
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)