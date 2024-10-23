from rest_framework import generics
from Hadiths.models import Hadith
from .serializers import HadithSerializer
from rest_framework import serializers
class HadithAPIView(generics.ListAPIView):
    queryset = Hadith.objects.all()
    serializer_class = HadithSerializer
class HadithCreateAPIView(generics.CreateAPIView):
    queryset = Hadith.objects.all()
    serializer_class = HadithSerializer
class HadithUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Hadith.objects.all()
    serializer_class = HadithSerializer
    lookup_field='id'
class HadithRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Hadith.objects.all()
    serializer_class = HadithSerializer
    lookup_field='id'
class HadithNarratorAPIView(generics.ListAPIView):
    queryset = Hadith.objects.all()
    serializer_class = HadithSerializer