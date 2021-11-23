from rest_framework import serializers
from .models import Lead

"""
Serializering our models.py so it can be return as a JSON format
for more info please go to: https://www.django-rest-framework.org/api-guide/serializers/
"""
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
