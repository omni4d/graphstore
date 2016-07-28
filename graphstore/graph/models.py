from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets


class NodeType(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class NodeTypeSerializer(ModelSerializer):
    class Meta:
        model = NodeType
        fields = ['name']


class NodeTypeViewSet(viewsets.ModelViewSet):
    queryset = NodeType.objects.all()
    serializer_class = NodeTypeSerializer
