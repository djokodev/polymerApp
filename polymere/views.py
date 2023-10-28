from rest_framework import viewsets
from .models import Reaction
from .serializers import ReactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#class ReactionViewSet(viewsets.ModelViewSet):
 #   queryset = Reaction.objects.all()
  #  serializer_class = ReactionSerializer

class HealthCheck(APIView):
    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)