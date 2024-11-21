from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin, \
    CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Artifact, Anomaly, Stalker
from .serializers import ArtifactSerializer, AnomalySerializer, StalkerSerializer


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


class StalkerListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Stalker.objects.all()
    serializer_class = StalkerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StalkerRetrieveView(GenericAPIView, RetrieveModelMixin):
    queryset = Stalker.objects.all()
    serializer_class = StalkerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)