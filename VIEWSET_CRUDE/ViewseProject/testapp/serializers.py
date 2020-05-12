from rest_framework import serializers
from testapp.models import Students
class StudentSerializer(serializers.ModelSerializer):
    model = Students
    fields = "__all__"
