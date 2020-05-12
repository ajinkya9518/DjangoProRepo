from rest_framework import serializers
from testapp.models import PersonalInfo

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = "__all__"
