from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question,Choice
from django.http import Http404
def index(request):
    latest_q_list=Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_q_list}
    return render(request,'polls/index.html',context)
def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question Does not exist')
    return render(request,'polls/detail.html',{'question':question})
def results(request,question_id):
    que=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':que})
def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
         sel_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
         return render(request,'polls/detail.html',{'question':question,
                                                      'error_message':'Please select choice and submit!'})
    else:
        sel_choice.votes+=1
        sel_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))