from rest_framework import viewsets
from .serializers import MyClassSerializer
from .models import MyClass

class MyClassviewsets(viewsets.ModelViewSet):

    serializer_class = MyClassSerializer
    queryset = MyClass.objects.all()

