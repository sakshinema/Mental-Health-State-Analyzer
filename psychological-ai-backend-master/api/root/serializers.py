from rest_framework import serializers

class EmotionSerializer(serializers.Serializer):
   neutral = serializers.FloatField()
   positive= serializers.FloatField()
   negative = serializers.FloatField()