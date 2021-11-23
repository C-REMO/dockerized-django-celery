import json
from django.http import JsonResponse
from rest_framework.views import APIView
from api.serializers import FeedRecordSerializer
from core.services.symbols import SymbolService


class AllSymbolsAPI(APIView):
    '''
    API EndPoint for all feeds of all types.
    Get all feeds.
    '''
    def get(self, request):
        """Get all feeds."""
        feeds = SymbolService.get_all()
        feed_serializer = FeedRecordSerializer(feeds, many=True)

        response = {
            'feeds': feed_serializer.data
        }
        return JsonResponse(response, safe=False)


class SymbolsByTypeAPI(APIView):
    '''
    API EndPoint for feeds of single type.
    Get feeds by type.
    '''
    def get(self, request, symbol_type):
        """Get feeds by type."""
        feeds = SymbolService.get_all_by_type(symbol_type)
        feed_serializer = FeedRecordSerializer(feeds, many=True)

        response = {
            'feeds': feed_serializer.data
        }
        return JsonResponse(response, safe=False)
