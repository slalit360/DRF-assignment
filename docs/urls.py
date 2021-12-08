from django.urls import path

from docs.swagger_views import schema_view

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='docs-api'),
]
