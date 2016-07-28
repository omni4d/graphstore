from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from graph.models import NodeTypeViewSet

urlpatterns = [url(r'^api-auth/', include('rest_framework.urls'))]

router = DefaultRouter()
router.register(r'NodeTypes', NodeTypeViewSet)

urlpatterns += router.urls
