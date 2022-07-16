from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from trivia.models import Question, Answer
from trivia.serializers import QuestionSerializer
import requests

from trivia_user.permissions import IsInRoleAdmin


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    @action(
        detail=False,
        methods=("post",),
        permission_classes=[IsInRoleAdmin, ],
    )
    def set_questions(self, request, *args, **kwargs):
        response = requests.get('https://opentdb.com/api.php?amount=10000')
        trivia_questions = response.json()['results']
        for question in trivia_questions:
            q = Question.objects.create(category=question['category'], question=question['question'])
            Answer.objects.create(question=q, answer=question['correct_answer'], is_correct=True)
            for answer in question['incorrect_answers']:
                Answer.objects.create(question=q, answer=answer, is_correct=False)

        return Response(status=status.HTTP_204_NO_CONTENT)
