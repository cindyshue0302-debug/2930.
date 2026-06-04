from django.contrib import admin
from .models import Question, QuizRecord

admin.site.register(Question)
admin.site.register(QuizRecord)