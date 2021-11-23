from rest_framework import viewsets, permissions
from .models import Lead
from .serializers import LeadSerializer

"""
Loading a viewset which allows us to get all methods e.g.GET, POST, DELETE etc
for more info please go to it's documentation: https://www.django-rest-framework.org/api-guide/viewsets/
"""
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()

    permission_classes = [ permissions.AllowAny ]

    serializer_class = LeadSerializer
