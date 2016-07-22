from django.db import models

class Question(models.Model):
    question_title=models.CharField(max_length=250)
    question=models.CharField(max_length=250)

    def __str__(self):
        return self.question_title
