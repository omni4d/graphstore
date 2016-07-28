from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet


class NodeType(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class NodeTypeSerializer(ModelSerializer):
    class Meta:
        model = NodeType
        fields = ['name']


class NodeTypeViewSet(ModelViewSet):
    queryset = NodeType.objects.all()
    serializer_class = NodeTypeSerializer
