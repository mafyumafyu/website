import datetime

from django.db import models
from django.utils import timezone

# Create your models here.



class Question(models.Model):
    def __str__(self) -> str:
        return self.text

    def was_published_recently(self) -> None:
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)

    text = models.CharField(max_length=200)
    publish_date = models.DateTimeField("date published")

class Choice(models.Model):
    def __str__(self) -> str:
        return self.text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)