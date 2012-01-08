from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext, loader

def index(request):
  return render_to_response('index.html', RequestContext(request))
