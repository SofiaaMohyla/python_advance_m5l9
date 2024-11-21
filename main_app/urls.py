from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtifactViewSet, AnomalyViewSet

router = DefaultRouter()
router.register(r'artifacts', ArtifactViewSet)
router.register(r'anomalies', AnomalyViewSet)
print(router.urls)
urlpatterns = [
    path('', include(router.urls)),

]