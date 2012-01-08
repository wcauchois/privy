from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext, loader
from decimal import Decimal
from models import Post, Board
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
  return render_to_response('index.html', RequestContext(request))

@csrf_exempt # XXX
def new_board(request):
  board = Board()
  board.radius = Decimal(request.POST['radius'])
  board.lat = Decimal(request.POST['lat'])
  board.lng = Decimal(request.POST['lng'])
  board.name = request.POST['name']
  board.save()
  return redirect('/')

def json_result(view):
  def view_prime(*args):
    return HttpResponse(json.dumps(view(*args)), mimetype='application/json')
  return view_prime

@json_result
def get_boards(request):
  top     = Decimal(request.GET['top'])
  bottom  = Decimal(request.GET['bottom'])
  left    = Decimal(request.GET['left'])
  right   = Decimal(request.GET['right'])
  boards = Board.objects.filter(lat__gte=min(top, bottom),
                                lat__lte=max(top, bottom),
                                lng__gte=min(left, right),
                                lng__lte=max(left, right))
  return [board.to_dict() for board in boards]

@csrf_exempt # XXX
def make_post(request, board_id):
  post = Post()
  post.board = get_object_or_404(Board, pk=board_id)
  post.content = request.POST['content']
  post.save()
  return redirect('/show_board/%s' % board_id)

def show_board(request, id):
  board = get_object_or_404(Board, pk=id)
  posts = Post.objects.filter(board=board)
  context = RequestContext(request, {
    'board': board,
    'posts': posts,
  })
  return render_to_response('show_board.html', context)

