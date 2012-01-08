from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext, loader
from decimal import Decimal
from models import Post, Board
from django.views.decorators.csrf import csrf_exempt

def index(request):
  return render_to_response('index.html', RequestContext(request))

@csrf_exempt # XXX
def new_board(request):
  board = Board()
  board.radius = Decimal(request.POST['radius'])
  board.center_lat = Decimal(request.POST['lat'])
  board.center_lng = Decimal(request.POST['lng'])
  board.name = request.POST['name']
  board.save()
  return redirect('/')

def show_board(request, board_id):
  locale = get_object_or_404(Locale, pk=board_id)
  Post.get(locale=locale)
  context = RequestContext(request, {
  })
  return render_to_response('show_board.html', context)

