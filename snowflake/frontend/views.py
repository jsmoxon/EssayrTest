from django.shortcuts import render_to_response

def first(request):
    return render_to_response('first.html')
