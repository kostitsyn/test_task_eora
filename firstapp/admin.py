from django.contrib import admin
from .models import Question, QuestionStep, User

admin.site.register(Question)
admin.site.register(QuestionStep)
admin.site.register(User)
