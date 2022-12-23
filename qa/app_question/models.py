from django.db import models
from django.contrib import admin


class NameUniqueModelMixin(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class NameModelMixin(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class GroupTest(NameUniqueModelMixin):
    description = models.TextField(verbose_name='описание', blank=True, null=True)

    class Meta:
        verbose_name = 'набор'
        verbose_name_plural = 'наборы'


class NameTest(NameUniqueModelMixin):
    group = models.ForeignKey(GroupTest, on_delete=models.CASCADE,
                              related_name='tests', verbose_name='группа')

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'


class Question(NameModelMixin):
    name_test = models.ForeignKey(NameTest, on_delete=models.CASCADE,
                              related_name='questions', verbose_name='тест')

    @admin.display(description='Кол-во ответов')
    def count_answears(self):
        return self.answers.count()

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


class AnAnswer(NameModelMixin):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answers', verbose_name='вопрос')
    right = models.BooleanField(default=False, verbose_name='Правильный ответ')

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'