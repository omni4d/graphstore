from django.db.models import Model, CharField, ForeignKey, CASCADE
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet


# Node Types
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


# Edge Types
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


# Nodes
class Node(Model):
    uuid = CharField(primary_key=True, max_length=64)
    node_type = ForeignKey(NodeType, on_delete=CASCADE)


class NodeSerializer(ModelSerializer):
    class Meta:
        model = Node
        fields = ['uuid', 'node_type']


class NodeViewSet(ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


# Edges
class Edge(Model):
    from_node = ForeignKey(
        Node, on_delete=CASCADE, related_name='outgoing_edge')
    to_node = ForeignKey(
        Node, on_delete=CASCADE, related_name='incoming_edge')
    edge_type = ForeignKey(EdgeType, on_delete=CASCADE)


class EdgeSerializer(ModelSerializer):
    class Meta:
        model = Edge
        fields = ['edge_type', 'from_node', 'to_node']


class EdgeViewSet(ModelViewSet):
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer
