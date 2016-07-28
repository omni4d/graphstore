from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from graph.models import NodeTypeViewSet, EdgeTypeViewSet

urlpatterns = [url(r'^api-auth/', include('rest_framework.urls'))]

router = DefaultRouter()
router.register(r'NodeTypes', NodeTypeViewSet)
router.register(r'EdgeTypes', EdgeTypeViewSet)

urlpatterns += router.urls
