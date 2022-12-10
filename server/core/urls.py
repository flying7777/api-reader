from django.contrib import admin
from django.urls import path, include


from .api import api


@api.get("/hello")
def hello(request):
    return "Hello world"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("api/auth/", include("accounts.urls")),
]


