from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from trivia_user.views import UserViewSet

router = SimpleRouter()
router.register("users", UserViewSet)

app_name = "Users"
urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
