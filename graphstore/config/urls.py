from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from graph.models import NodeTypeViewSet

router = DefaultRouter()
router.register(r'graph', NodeTypeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
