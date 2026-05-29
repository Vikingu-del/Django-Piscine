from django.contrib import admin
from .models import Question, Choice


# This tells Django: "Choices should be edited on the same page as the Question"
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        (
            "Date information",
            {"fields": ["pub_date"], "classes": ["collapse"]},
        ),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_per_page = 1
    date_hierarchy = "pub_date"


admin.site.register(Question, QuestionAdmin)

# Register your models here.
