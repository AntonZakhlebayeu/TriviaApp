from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("trivia_user.urls", namespace="authentication")),
    path("api/", include("trivia.urls", namespace="question")),
]
