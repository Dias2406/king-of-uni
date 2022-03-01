''''
Provides views for team joining,
Will provide views for team creation and leaving
'''
from django.shortcuts import render, redirect
from django.contrib import messages
from group.forms import JoinGroup
from group.models import Group

__author__ = "Joseph Cato"

def group(request):

    user = request.user

    context = {
        "user" : user,
    }

    return render(request, 'group/group.html', context)


def join_group(request):
    context = {

    }
    user = request.user
    if not user.is_authenticated:
        return redirect('login')


    #TODO - below seems to have no effect not sure why
    # Handles form submission - Lets user join group if it exsists, sends an error otherwise
    groups = Group.objects.all()
    if (request.POST == True):

        form = JoinGroup(request.POST)

        if form.is_valid():
            group_name = request.POST['belongs_to_group']

            if group_name in groups:
                user.belongs_to_group = group_name
                user.save()

            else:
                messages.error(request, 'No such group')

    else:
        form = JoinGroup()
        
    context['form'] = form
    return render(request, 'group/group.html', context)

def leave_group(request):

    user = request.user

    

    #TODO

    context = {

    }

    return render(request, 'group/leave_group.html', context)
