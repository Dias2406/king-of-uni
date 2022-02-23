from django.shortcuts import render, redirect

# Create your views here.

def game_keeper_view(request):
    return render(request, 'game/game_keeper.html', {})
