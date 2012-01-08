from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext, loader
from models import Post, Locale

def index(request):
  return render_to_response('index.html', RequestContext(request))

def show_board(request, board_id):
  locale = get_object_or_404(Locale, pk=board_id)
  Post.get(locale=locale)
  context = RequestContext(request, {
  })
  return render_to_response('show_board.html', context)

