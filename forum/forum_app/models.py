from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Question(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    questionContent = RichTextUploadingField(blank=True,config_name='special')
    questionTitle = models.CharField(max_length=120, null=True)
    acceptanceStatus = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)


