from django.contrib import admin
from .models import Question,Choice

admin.site.site_header="THE VOTING SYSTEM"
admin.site.site_title="Voting Admin Arena"
admin.site.index_title="Welcome to the Admin area"
class ChoiceInLine(admin.TabularInline):
    model=Choice
    extra=3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None, {'fields':['text']}),
               ('Date Information',{'fields':['pub_date'],'classes':['collapse']})]
    inlines=[ChoiceInLine]
admin.site.register(Question,QuestionAdmin)
