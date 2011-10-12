from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from frontend.models import Entry, Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render_to_response('blogonymous/homepage.html')


def yeah(request):
    return render_to_response('blogonymous/first.html')

def home(request):
    entries = Response.objects.order_by('question')
    p = Entry.objects.order_by('answers')
    return render_to_response("blogonymous/home.html", {"entries": entries, "p": p})

def detail(request, entry_id):
    p = get_object_or_404(Entry, pk=entry_id)
    return render_to_response('blogonymous/response_form.html', {"p": p}, context_instance=RequestContext(request))

def submit(request, entry_id):
    p = get_object_or_404(Entry, pk=entry_id)
    return render_to_response('blogonymous/submit.html', {"p": p}, context_instance=RequestContext(request))

def single(request, entry_id):
    p = get_object_or_404(Entry, pk=entry_id)
    q = p.response_set.order_by('votes')
    return render_to_response('blogonymous/single.html', {'p': p, 'q':q}, context_instance=RequestContext(request))

#submits a response to an entry
def enter(request, entry_id):
    p = get_object_or_404(Entry, pk=entry_id) 
    entry = p.response_set.create(headline=request.POST['headline'])
    entry.save()
    entry.body_text = request.POST['body_text']
    entry.save()
    p.answers += 1
    p.save()
    return HttpResponseRedirect(reverse('frontend.views.single', args=(p.id,)))

#upvote
def upvote(request, entry_id):
    p = get_object_or_404(Entry, pk=entry_id)
    selected_response = p.response_set.get(pk=request.POST['headline'])
    selected_response.votes += 1
    selected_response.save()
    return HttpResponseRedirect(reverse('frontend.views.single', args=(p.id,)))

def blog_post(request, entry_id, answer_id):
    p = get_object_or_404(Entry, pk=entry_id)
    q = get_object_or_404(Response, pk=answer_id)
    return render_to_response('blogonymous/post.html', {"p":p, "q":q})
    

def question(request):
    return render_to_response('blogonymous/question.html', context_instance=RequestContext(request))

def question_submit(request):
    new = Entry.objects.create(question=request.POST['question'])
    new.save()
    new.desc = request.POST['desc']
    new.save()
    return HttpResponseRedirect(reverse('frontend.views.home'))

def about(request):
    return render_to_response('blogonymous/about.html')
