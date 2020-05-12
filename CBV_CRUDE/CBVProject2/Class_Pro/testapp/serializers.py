from rest_framework import serializers
from .models import Newspaper

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = "__all__"
