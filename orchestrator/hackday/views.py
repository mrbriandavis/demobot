# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods

from hackday.models import Poll
try:
     import json
except ImportError:
     import simplejson as json


def index(request):
    # return HttpResponse("Hello, world. You're at the poll index.")
    from hackday.tasks import add
    from celery import group

    jobs = []

    for x in range(1,10):
        st = add.subtask((1, x))
        jobs.append(st)

    job = group(jobs)
    result = job.apply_async()
    res = result.join()
    return render_to_response('index.html', {'poll': result})

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

#@require_http_methods(['POST'])
def event(request, event):
    d = {'success': 5,
         '6': 7}

#    return HttpResponse(json.dumps(d, sort_keys=True, indent=2), content_type='application/json')
    return HttpResponse(event, content_type='application/json')


