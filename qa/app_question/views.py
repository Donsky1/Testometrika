from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
import json

from .models import GroupTest, NameTest, Question, AnAnswer
from .serializers import NameTestSerializer, GroupTestSerializer


class IndexView(generic.ListView):
    model = GroupTest
    template_name = 'app_question/index.html'
    context_object_name = 'testkit'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(object_list=None, **kwargs)
        return context


# gets dynamically test list from ajax request
def get_tests(request):
    kit_id = request.GET.get('kit_id')
    current_kit = GroupTest.objects.get(id=kit_id)
    tests = current_kit.tests.all()
    serializer = NameTestSerializer(tests, many=True)
    return JsonResponse(serializer.data, safe=False)


# check completion status test after receiving, send request
def test_is_done(index: int, list_idxs: list):
    return int(index) == list_idxs[-1]


# view function to open page of test, main block
@login_required
def play_test(request, pk):
    # get current test
    object_test = get_object_or_404(NameTest, pk=pk)
    # if we have current test in session, get him, else false
    session = request.session.get(str(pk), False)
    # get all questions
    all_questions_for_test = object_test.questions.all()
    # get ids all questions for checking status
    question_ids = sorted([q.id for q in all_questions_for_test])

    # checking: if we don't have questions, redirect to index page
    if not question_ids:
        return HttpResponseRedirect('/')

    # if we got GET request
    if request.method == 'GET':
        if session:
            # if session have test, get last test id
            last_question_id = list(session)[-1]
            # if test done, redirect to result page with test result from session
            if test_is_done(last_question_id, question_ids):
                res = session
                return HttpResponseRedirect(reverse_lazy('result', args=[res]))
            id_question = last_question_id
        else:
            # if the user passes the test for the first time, get 0 id in ids list
            id_question = question_ids[0]
        #     get queryset from current id test
        current_question = Question.objects.get(pk=id_question)
    else:
        # if we got POST request
        if not session:
            # and we don't have session current test
            request.session[str(pk)] = {}

        # get id current test
        cur_question_id = request.POST.get('cur_question_id')
        #  write in session
        request.session[str(pk)][cur_question_id] = request.POST.getlist('choice')
        #  modify session, save data in session
        request.session.modified = True

        # if test done, redirect to result page
        if test_is_done(cur_question_id, question_ids):
            res = request.session[str(pk)]
            return HttpResponseRedirect(reverse_lazy('result', args=[res]))

        # if test not done, get next id test, and go on
        cur_question_id_index = question_ids.index(int(cur_question_id))
        next_question = Question.objects.get(pk=question_ids[cur_question_id_index + 1])
        current_question = next_question
    return render(request, 'app_question/play_test.html',
                  {'object_test': object_test, 'current_question': current_question})


# view which give us result page
def result(request, res):
    res = json.loads(res.replace("\'", "\""))
    count_true = 0
    total = 0
    result_dict = {}
    result_dict_val = {}
    for question_id, answer_id in res.items():
        total += 1
        current_question = Question.objects.get(id=question_id)
        true_answers_ids = [answer.name for answer in current_question.answers.filter(right=True)]
        answers_ids = [AnAnswer.objects.get(id=id).name for id in answer_id]
        result_dict[current_question.name] = [answers_ids, true_answers_ids]
        if answers_ids == true_answers_ids:
            count_true += 1
    result_dict_val['count_true'] = count_true
    result_dict_val['count_false'] = total - count_true
    result_dict_val['total'] = total
    result_dict_val['percent_true_answers'] = round(count_true / total, 2) * 100
    return render(request, 'app_question/result.html', {'result': result_dict,
                                                        'result_dict_val': result_dict_val})


def clear_current_session(request, pk):
    del request.session[str(pk)]
    return HttpResponseRedirect(reverse_lazy('play-test', args=[pk]))


# before test page. checking test
# give result page or open last done question test page
def check(request, pk):
    object_test = get_object_or_404(NameTest, pk=pk)
    session = request.session.get(str(pk), False)
    all_questions_for_test = object_test.questions.all()
    question_ids = sorted([q.id for q in all_questions_for_test])
    if not session:
        return HttpResponseRedirect(reverse_lazy('play-test', args=[pk]))
    else:
        last_question_id = list(session)[-1]
        res = json.dumps(session) if test_is_done(last_question_id, question_ids) else None
    return render(request, 'app_question/check.html',
                  {'object_test': object_test, 'res': res})
