from rest_framework import serializers

from shortener.models import ShortURL


class CreateShortURLSerializer(serializers.ModelSerializer):
    """Serializer for creating ShortURL objects."""

    class Meta:
        """Metaclass."""

        model = ShortURL
        fields = ["original_url"]


class ResponseShortURLSerializer(serializers.Serializer):
    """Serializer for the response of the ShortURL object."""

    short_url = serializers.URLField()


class ResolveShortURLSerializer(CreateShortURLSerializer):
    """Serializer for resolving ShortURL objects."""

    class Meta(CreateShortURLSerializer.Meta):
        """Metaclass."""

        pass
