from django.forms import BaseInlineFormSet
from django import forms
from django.utils.translation import gettext as _


class ChoicesInlineFormSet(BaseInlineFormSet):

    def clean(self):
        true_test_count = 0
        total_tests = 0
        for form in self.forms:
            if not form.cleaned_data.get('DELETE'):
                total_tests += 1
                if form.cleaned_data.get('right'):
                    true_test_count += 1

        if total_tests == 1:
            raise forms.ValidationError(_('Ошибка: Необходимо минимум 2 варианта ответа'))

        if true_test_count:
            pass
        else:
            raise forms.ValidationError(_('Ошибка: должен быть хотябы 1 правильный вариант'))

        if total_tests == true_test_count:
            raise forms.ValidationError(_('Ошибка: все варианты не могут быть правильными. '
                                          'Добавьте хотябы один неправильный вариант'))