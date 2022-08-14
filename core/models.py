from django.db import models
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                null=True)
    title = models.CharField(max_length=200)
    body = models.TextField(verbose_name='Detailed description')
    created_at = models.DateTimeField(auto_now_add=True)
    # finished_at = models.DateTimeField(null=True, blank=True, default=False)

    def __str__(self):
        f'{self.author}: question {self.pk}'

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)