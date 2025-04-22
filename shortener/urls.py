from django.urls import path

from shortener.views import CreateShortURLView, ResolveShortURLView

urlpatterns = [
    path("shorten", CreateShortURLView.as_view(), name="create-short-url"),
    path(
        "resolve/<slug:short_code>",
        ResolveShortURLView.as_view(),
        name="resolve-short-url",
    ),
]
