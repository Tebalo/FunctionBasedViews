# import the standard Django Model
# from built-in library
from django.db import models

# Create your models here.


class GeeksModel(models.Model):
    # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()
    # renames the instances of the model
    # with their title name

    def __str__(self):
        return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
