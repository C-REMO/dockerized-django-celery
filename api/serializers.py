from rest_framework import serializers
from symbols.models import FeedRecord


class FeedRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedRecord
        fields = (
            'title', 'description', 'url'
        )
