from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from datetime import date


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=True, methods=['GET'])
    def done(self, request, pk=None):
        todo = self.get_object()
        todo.completed_at = date.today()
        todo.save()
        return Response(self.get_serializer(todo).data)