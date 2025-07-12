from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Retrieve all properties from cache if available, otherwise fetch from database.
    Caches the result for 1 hour (3600 seconds).
    """
    # Try to get properties from cache
    properties = cache.get('all_properties')
    
    # If not in cache, fetch from database and cache it
    if properties is None:
        properties = Property.objects.all()
        cache.set('all_properties', properties, 3600)  # Cache for 1 hour
    
    return properties
