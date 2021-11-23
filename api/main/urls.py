from rest_framework import routers
from .api import LeadViewSet

# Setting an api endpoint

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls
