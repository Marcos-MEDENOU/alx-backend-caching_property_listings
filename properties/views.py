from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Property
from .serializers import PropertySerializer

@api_view(['GET'])
@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    """
    List all properties with caching enabled.
    The response will be cached for 15 minutes.
    """
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)
