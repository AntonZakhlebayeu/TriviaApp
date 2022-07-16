from django.db import models


class Question(models.Model):
    category = models.CharField(max_length=50)
    question = models.TextField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
    is_correct = models.BooleanField()
    answered_user = models.ForeignKey('trivia_user.User', on_delete=models.CASCADE, related_name='answered_user')

    def __str__(self):
        return self.answer
