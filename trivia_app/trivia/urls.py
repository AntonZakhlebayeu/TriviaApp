from django.urls import path, include
from rest_framework import routers

from trivia import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
app_name = "questions"

urlpatterns = [
    path('', include(router.urls)),
]
