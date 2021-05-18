from rest_framework import permissions
from rest_framework import generics
from .models import Alias
from .serializers import AliasSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class AliasList(generics.ListCreateAPIView):
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer


class AliasDetail(generics.UpdateAPIView):
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer

    # override the the delete function to use soft delete
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
