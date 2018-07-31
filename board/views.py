from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib import messages

from board.models import Board
from board.forms import BoardForm
from main.views import admin_required


class BoardDetailView(DetailView):
    queryset = Board.objects.all()
    template_name = 'board/try.html'


def board(request):
    '''
    get the board object and show on board page
    '''
    boards = Board.objects.all()
    return render(request, 'board/board.html', {'boards': boards})


@admin_required
def create_board(request):
    '''
    Create a new board instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the board page
    '''
    template = 'board/create_update_board.html'
    if request.method == "GET":
        return render(request, template, {'form': BoardForm()})

    # POST
    form = BoardForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form': form})
    form.save()
    messages.success(request, '公告已新增')
    return redirect('board:board')


@admin_required
def update_board(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    template = 'board/create_update_board.html'
    if request.method == "GET":
        form = BoardForm(instance=board)
        return render(request, template, {'form': form})

    # POST
    form = BoardForm(request.POST, instance=board)
    if not form.is_valid():
        return render(request, template, {'form': form})
    form.save()
    messages.success(request, '公告已修改')
    return redirect('board:board')


@admin_required
def delete_board(request, board_id):
    if request.method == 'GET':
        return board(request)

    board = get_object_or_404(Board, id=board_id)
    board.delete()
    messages.success(request, '公告已刪除')
    return redirect('board:board')
