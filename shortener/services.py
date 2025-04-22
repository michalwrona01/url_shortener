import secrets
import string

from django.db import transaction
from django.http import HttpRequest

from shortener.models import ShortURL
from shortener.selectors import ShortURLSelector


class ShortURLService:
    """ShortURLService class"""

    model = ShortURL
    selector = ShortURLSelector

    @classmethod
    @transaction.atomic
    def create_short_url(cls, *, request: HttpRequest, original_url: str) -> str:
        """Create a short URL from the given URL.

        :param request: The HTTP request.
        :param original_url: The original URL.

        :return: The short URL.
        """
        generated_code = cls._generate_short_code()
        while cls.selector.is_exists_short_code(short_code=generated_code):
            generated_code = cls._generate_short_code()
        cls.model.objects.create(original_url=original_url, short_code=generated_code)
        return request.build_absolute_uri(f"/{generated_code}")

    @classmethod
    def _generate_short_code(cls, *, length: int = 6):
        """Returns random code

        :param length: length of code
        :return: str: random code
        """

        return "".join(
            secrets.choice(string.ascii_letters + string.digits) for _ in range(length)
        )
