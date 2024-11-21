from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtifactViewSet, AnomalyViewSet, StalkerListCreateView, StalkerRetrieveView

router = DefaultRouter()
router.register(r'artifacts', ArtifactViewSet)
router.register(r'anomalies', AnomalyViewSet)
print(router.urls)
urlpatterns = [
    path('stalkers/', StalkerListCreateView.as_view(), name='stalker-list-create'),
    path('stalkers/<int:pk>/', StalkerRetrieveView.as_view(), name='stalker-detail'),
    path('', include(router.urls)),

]