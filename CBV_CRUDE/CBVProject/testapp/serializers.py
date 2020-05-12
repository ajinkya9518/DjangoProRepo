from rest_framework import serializers
from testapp.models import Newspaper
class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = '__all__'
