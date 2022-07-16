from django.db import models
from django.db.models.fields import related


class Question(models.Model):
    category = models.CharField(max_length=50)
    question = models.TextField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.answer


class AnsweredQuestions(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='user_answer')
    answered_user = models.ForeignKey('trivia_user.User', on_delete=models.CASCADE, related_name='answered_user')
    is_correct = models.BooleanField()
