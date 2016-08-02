from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from graphstore.graph.models import (
    NodeTypeViewSet, EdgeTypeViewSet, NodeViewSet, EdgeViewSet)

urlpatterns = [url(r'^api-auth/', include('rest_framework.urls'))]
router = DefaultRouter()

routes = {
    'NodeTypes': NodeTypeViewSet,
    'EdgeTypes': EdgeTypeViewSet,
    'Nodes': NodeViewSet,
    'Edges': EdgeViewSet
}

for route, viewset in routes.items():
    router.register(route, viewset)

urlpatterns += router.urls
