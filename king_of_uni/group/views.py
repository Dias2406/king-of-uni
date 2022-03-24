"""
Provides views for creating and joining grouos
"""
from django.shortcuts import render, redirect
from group.forms import CreateGroupForm
from group.models import Group
from account.models import Account
from django.contrib import messages

__author__ = "Joseph Cato"

# Create your views here.
def group_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    group = user.belongs_to_group
    group_members = Account.objects.filter(belongs_to_group=group).order_by('-score')
    context['members'] = group_members


    return render(request, 'group/group.html', context)

def groups_list_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    groups = Group.objects.all()
    context['groups'] = groups


    return render(request, 'group/groups_list.html', context)

def create_group_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    form = CreateGroupForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = CreateGroupForm()
        return redirect('game_keeper:groups_list')
    context['form'] = form
    return render(request, 'group/create_group.html', context)

def join_group_view(request):
    context = {}
    groups = Group.objects.all()
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    if request.POST:
        try:      
            group_name = request.POST['belongs_to_group']
            group = Group.objects.get(name=group_name)
            user.belongs_to_group = group
            user.is_inTeam = True
            user.save()
            return redirect('group:group_info')
        except Group.DoesNotExist:
            messages.error(request, 'No such group') 
    else:
        context['groups'] = groups


    return render(request, 'group/join_group.html', context)

def leave_group_view(request):
    user = request.user
    user.is_inTeam = False
    user.belongs_to_group = None
    user.save()
    return redirect('group:group_info')