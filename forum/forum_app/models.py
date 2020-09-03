from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    questionContent = RichTextUploadingField(blank=True,config_name='special')
    questionTitle = models.CharField(max_length=120, null=True)
    acceptanceStatus = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerContent = models.CharField(max_length=300)
    acceptanceStatus = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)

class QuestionComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    commentContent = models.CharField(max_length=300)
    createdDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.commentContent

class AnswerComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    commentContent = models.CharField(max_length=300)
    createdDate = models.DateTimeField(default=timezone.now)

class AnswerPoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    Upvote = models.BooleanField(default=False)
    Downvote = models.BooleanField(default=False)
    acceptanceStatus = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)

class QuestionPoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Upvote = models.BooleanField(default=False)
    Downvote = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)

class TagDetails(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    TagName = models.CharField(max_length=25)



