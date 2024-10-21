from rest_framework import serializers
from Hadiths.models import Hadith
class HadithSerializer(serializers.ModelSerializer):
    class Meta:
         model = Hadith
         fields = ('id',"narrator", "text", "explantion")