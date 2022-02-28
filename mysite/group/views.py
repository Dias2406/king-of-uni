from email.policy import default
from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect 

from account.models import Account
from group.forms import JoinGroup
from group.models import Group

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
    #TODO - seems to have no effect not sure why
    groups = Group.objects.all()
    if (request.POST == True):
        print(request.GET['name'])
        form = JoinGroup(request.POST)
        if form.is_valid():
            # my comments Dias
            group_name = request.POST['belongs_to_group']
            if group_name in groups:
                user.belongs_to_group = group_name
                user.save()
                #do not need below code ____
                #Group, created = Group.objects.get_or_create(
                    #request.GET['name'],
                   # defaults = None
               # )
            else:
                messages.error(request, 'No such group')
     else:
        form = JoinGroup()
        
    context['form'] = form
    return render(request, 'group/group.html', context)



        #    for e in Group.objects.all():
        #        #If group exsists, joins group
        #        if ( e.name == request.GET['name']):
        #            request.user.belongs_to_group.add(e)
        #            return render(request, 'group/group.html', context)
        #
        #    # Creates new group, set owner and name
        #    group_instance = Group.objects.create(name = request.GET['name'], owner=request.user)
        #    # User joins created group
        #    request.user.belongs_to_group.add(group_instance)
        #    return render(request, 'group/group.html', context)
            

                    

        

    return render(request, 'group/join_group.html', context)

def leave_group(request):

    user = request.user

    

    #TODO

    context = {

    }

    return render(request, 'group/leave_group.html', context)
