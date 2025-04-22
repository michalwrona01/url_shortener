from django.http import HttpResponseRedirect
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shortener.selectors import ShortURLSelector
from shortener.serializers import (CreateShortURLSerializer,
                                   ResolveShortURLSerializer,
                                   ResponseShortURLSerializer)
from shortener.services import ShortURLService


class CreateShortURLView(APIView):
    """CreateShortURLView class"""

    serializer_create = CreateShortURLSerializer
    serializer_response = ResponseShortURLSerializer
    service = ShortURLService

    @swagger_auto_schema(
        request_body=CreateShortURLSerializer(many=False),
        responses={status.HTTP_201_CREATED: ResponseShortURLSerializer(many=False)},
    )
    def post(self, request, *args, **kwargs):
        """Create a short URL from the given URL."""

        serializer = self.serializer_create(data=request.data)
        serializer.is_valid(raise_exception=True)
        short_url = self.service.create_short_url(
            request=request, original_url=serializer.validated_data["original_url"]
        )
        serializer = self.serializer_response({"short_url": short_url})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ResolveShortURLView(APIView):
    """ResolveShortURLView class"""

    serializer_response = ResolveShortURLSerializer
    service = ShortURLService
    selector = ShortURLSelector

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: ResolveShortURLSerializer(many=False)}
    )
    def get(self, request, short_code):
        obj = self.selector.get_short_url(short_code=short_code)
        serializer = self.serializer_response({"original_url": obj.original_url})
        return Response(serializer.data, status=status.HTTP_200_OK)


class RedirectToOriginalURLView(APIView):
    """RedirectToOriginalURLView class"""

    selector = ShortURLSelector

    @swagger_auto_schema(
        responses={status.HTTP_302_FOUND: "Redirected to original URL"}
    )
    def get(self, request, short_code):
        obj = self.selector.get_short_url(short_code=short_code)
        return HttpResponseRedirect(obj.original_url)
