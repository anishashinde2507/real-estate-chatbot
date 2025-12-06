"""
Serializers for API requests and responses.
"""

from rest_framework import serializers


class QueryRequestSerializer(serializers.Serializer):
    """Serializer for user query request."""
    message = serializers.CharField(max_length=500, required=True)


class ChartDataSerializer(serializers.Serializer):
    """Serializer for chart data."""
    years = serializers.ListField(child=serializers.CharField())
    values = serializers.ListField(child=serializers.IntegerField(), required=False)
    areas = serializers.DictField(required=False)


class QueryResponseSerializer(serializers.Serializer):
    """Serializer for query response - supports both single and comparison modes."""
    type = serializers.CharField(required=False)
    area = serializers.CharField(required=False, allow_blank=True)
    areas = serializers.ListField(required=False)
    summary = serializers.CharField()
    chart = ChartDataSerializer()
    table = serializers.ListField(required=False)
    tables = serializers.DictField(required=False)
