from django.contrib import admin

from .models import GroupTest, NameTest, Question, AnAnswer
from .forms import ChoicesInlineFormSet


class AnAnswerInline(admin.TabularInline):
    model = AnAnswer
    extra = 0
    formset = ChoicesInlineFormSet


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    show_change_link = True
    template = 'admin/app_question/question_tabular_template.html'


class NameTestInline(admin.TabularInline):
    model = NameTest
    extra = 0
    show_change_link = True


@admin.register(GroupTest)
class GroupTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ['id']
    inlines = [NameTestInline]


@admin.register(NameTest)
class NameTestAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_test', 'count_answears')
    list_display_links = ('id', 'name')
    inlines = [AnAnswerInline]
    search_fields = ('name', )