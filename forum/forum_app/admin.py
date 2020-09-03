from django.contrib import admin
from .models import Question,QuestionComment,QuestionPoint,Answer,AnswerComment,AnswerPoint, TagDetails

admin.site.register(Question)
admin.site.register(QuestionComment)
admin.site.register(QuestionPoint)
admin.site.register(Answer)
admin.site.register(AnswerComment)
admin.site.register(AnswerPoint)
admin.site.register(TagDetails)
