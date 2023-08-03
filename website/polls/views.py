from django.http import Http404, HttpResponse 
from django.shortcuts import get_object_or_404, render

from .models import Choice, Question

# Create your views here.

def index(request) -> None:
    latest_question_list = Question.objects.order_by("-publish_date")[:5]

    context = {
        "latest_question_list": latest_question_list
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id) -> None:
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request, 'polls/detail.html', {"question": question})

def results(request, question_id) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id) -> HttpResponse:
    response = "You voted on question %s."
    return HttpResponse(response % question_id)