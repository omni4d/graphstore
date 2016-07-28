from django.db.models import Model, CharField
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet


class NodeType(Model):
    name = CharField(max_length=12)

    def __str__(self):
        return self.name


class NodeTypeSerializer(ModelSerializer):
    class Meta:
        model = NodeType
        fields = ['name']


class NodeTypeViewSet(ModelViewSet):
    queryset = NodeType.objects.all()
    serializer_class = NodeTypeSerializer


class EdgeType(Model):
    name = CharField(max_length=12)

    def __str__(self):
        return self.name


class EdgeTypeSerializer(ModelSerializer):
    class Meta:
        model = EdgeType
        fields = ['name']


class EdgeTypeViewSet(ModelViewSet):
    queryset = EdgeType.objects.all()
    serializer_class = EdgeTypeSerializer
