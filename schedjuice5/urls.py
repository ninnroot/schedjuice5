"""schedjuice5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Schedjuice API",
        default_version="v2",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(
        "api/v2/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/v2/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("api/v2/admin/", admin.site.urls),
    path("api/v2/", include("app_docs.urls")),
    path("api/v2/", include("app_auth.urls")),
    path("api/v2/", include("app_finance.urls")),
    path("api/v2/", include("app_users.urls")),
    path("api/v2/", include("app_utils.urls")),
    path("api/v2/", include("app_course.urls")),
    path("api/v2/", include("app_campus.urls")),
    path("api/v2/", include("app_management.urls")),
    path("api/v2/", include("app_announcement.urls")),
    path("api/v2/", include("app_assignment.urls")),
    path("api/v2/ws/", include("app_ws.urls")),
    path("api/v2/docs/", include("models_docs.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    try:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
    except ImportError:
        pass
