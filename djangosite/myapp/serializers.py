from rest_framework import serializers
from . import models as myapp_models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = myapp_models.Student
        fields = '__all__'
