from django.contrib import admin

from .models import Question, Choice, Vote

class QuestionAdmin(admin.ModelAdmin):

    class Meta:
		model = Question

admin.site.register(Question,QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):

    class Meta:
		model = Choice

admin.site.register(Choice,ChoiceAdmin)

class VoteAdmin(admin.ModelAdmin):

    class Meta:
		model = Vote

admin.site.register(Vote,VoteAdmin)
