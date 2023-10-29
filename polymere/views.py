from rest_framework import viewsets
from .models import Polymer
from datetime import datetime
from .serializers import PolymerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from polymere import factory
from dateutil.parser import isoparse
from django.utils.timezone import make_aware




class HealthCheck(APIView):
  def get(self, request):
      return Response({}, status=status.HTTP_200_OK)
   
  def get_extra_actions():
    return []
    


class Polymers(viewsets.ModelViewSet):
  queryset = Polymer.objects.all()
  serializer_class = PolymerSerializer

  def is_valid_polymer(self, polymer):
     if 1 <= len(polymer) <= 128:
      return True
     else:
       return False

  def create(self, request):
    if request.method == "POST":
      polymers = request.data
       
      for polymer_entry in polymers:
        timestamp = polymer_entry.get("timestamp")
        polymer = polymer_entry.get("polymer")

        try:
          timestamp = make_aware(timestamp)
        except ValueError:
          return Response("Le format du timestamp est invalide", status=status.HTTP_400_BAD_REQUEST)
        
        if not self.is_valid_polymer(polymer):
          return Response("Le polymère est invalide. Veuillez fournir un polymère d'une longueur comprise entre 1 et 128")

        if Polymer.objects.filter(timestamp=timestamp).exists():
          return Response("Un polymère existe déjà pour l'heure donnée.", status=status.HTTP_400_BAD_REQUEST)   
        
        #try:
          #polymer = factory.processing_plant(polymer)
        #except ValueError as e:
          #return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
          
        Polymer.objects.create(timestamp=timestamp, polymer=polymer)

      return Response("Création réussie de polymères.", status=status.HTTP_201_CREATED)

  def list(self, request):
    if request.method == "GET":
      start = request.query_params.get('start')
      end = request.query_params.get('end')

      if not start or not end:
        return Response("Les horodatages de début et de fin doivent être fournis.", status=status.HTTP_400_BAD_REQUEST)
      
      try:
        start = isoparse(start)
        end = isoparse(end)
      except ValueError:
        return Response("Le format du timestamp est invalide", status=status.HTTP_400_BAD_REQUEST)
      
      polymers = Polymer.objects.filter(timestamp__range=(start, end))

      polymer_entries = []

      for polymer in polymers:
        polymer_entry = {
          'timestamp': polymer.timestamp,
          'polymer': polymer.polymer
        }
        polymer_entries.append(polymer_entry)

    return Response(polymer_entries)
  
  def get_extra_actions():
    return []
  
  
  
class ReactedPolymer(viewsets.ModelViewSet):
  def list(self, request):
    queryset = Polymer.objects.all()
    serializer_class = PolymerSerializer
    pass