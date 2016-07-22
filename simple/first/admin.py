from django.contrib import admin
from .models import Question

class QuestionA(admin.ModelAdmin):
    fields=['question_title','id']
    list_display=('question','question_title','pk')
    list_filter=['question']
    search_fields=['question_title',]

admin.site.register(Question,QuestionA)

# Register your models here.
