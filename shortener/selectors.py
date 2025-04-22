from django.shortcuts import get_object_or_404

from shortener.models import ShortURL


class ShortURLSelector:
    """ShortURLSelector class"""

    model = ShortURL

    @classmethod
    def is_exists_short_code(cls, *, short_code: str) -> bool:
        """Check if a short code exists in the database.

        :param short_code: The short code to check.

        :return: True if the short code exists, False otherwise."""
        return cls.model.objects.filter(short_code=short_code).exists()

    @classmethod
    def get_short_url_by_short_code(cls, *, short_code: str) -> ShortURL:
        """Get a short URL from the database.

        :param short_code: The short code of the ShortURL.

        :return: The ShortURL object.
        """
        return get_object_or_404(cls.model, short_code=short_code)
