from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from frontend.models import Entry, Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    entries = Response.objects.order_by('question')
    p = Entry.objects.order_by('answers')
    return render_to_response("home.html", {"entries": entries, "p": p})

#shows a single question and text box for response
def submit(request, entry_id):
    p = get_object_or_404(Entry, pk=entry_id)
    return render_to_response('submit.html', {"p": p}, context_instance=RequestContext(request))

#show question of the day as the home page. Change pk to change question
def question_of_day(request):
    p = get_object_or_404(Entry, pk=3)
    return render_to_response('submit.html', {"p": p}, context_instance=RequestContext(request))

#shows a question and all of its responses
def single(request, entry_id):
    p = get_object_or_404(Entry, pk=entry_id)
    q = p.response_set.order_by('votes')
    return render_to_response('single.html', {'p': p, 'q':q}, context_instance=RequestContext(request))

#submits a response to an entry
def enter(request, entry_id):
    p = get_object_or_404(Entry, pk=entry_id) 
    first_sentence = request.POST['body_text']
    entry = p.response_set.create(headline=first_sentence[:20])
    entry.save()
    entry.body_text = request.POST['body_text']
    entry.save()
    p.answers += 1
    p.save()
    return HttpResponseRedirect(reverse('frontend.views.single', args=(p.id,)))

#shows a single response in full/
def blog_post(request, entry_id, answer_id):
    p = get_object_or_404(Entry, pk=entry_id)
    q = get_object_or_404(Response, pk=answer_id)
    return render_to_response('post.html', {"p":p, "q":q})

#upvote
def upvote(request, entry_id):
    p = get_object_or_404(Entry, pk=entry_id)
    selected_response = p.response_set.get(pk=request.POST['headline'])
    selected_response.votes += 1
    selected_response.save()
    return HttpResponseRedirect(reverse('frontend.views.single', args=(p.id,)))

#upvote post
def upvote_post(request, entry_id, answer_id):
    p = get_object_or_404(Entry, pk=entry_id)
    selected_response = p.response_set.get(pk=answer_id)
    selected_response.votes += 1
    selected_response.save()
    return HttpResponseRedirect(reverse('frontend.views.blog_post', args=(p.id,selected_response.id)))

#shows question submission form
def question(request):
    return render_to_response('question.html', context_instance=RequestContext(request))

#submits question
def question_submit(request):
    new = Entry.objects.create(question=request.POST['question'])
    new.save()
    new.desc = request.POST['desc']
    new.save()
    return HttpResponseRedirect(reverse('frontend.views.home'))

def about(request):
    return render_to_response('about.html')
    
def pk(request):
    return render_to_response('pk.html')
