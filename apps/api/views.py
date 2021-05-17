from rest_framework import permissions
from rest_framework import generics
from .models import Alias
from .serializers import AliasSerializer

# Create your views here.


class AliasList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer


class AliasDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer
