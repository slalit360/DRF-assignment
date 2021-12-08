from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Query-Assignment",
        default_version='1.0',
        description="assignment",
        terms_of_service="",
        contact=openapi.Contact(email="slalit360@gmail.com"),
        license=openapi.License(name="XYZ"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
