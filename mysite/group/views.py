from django.shortcuts import render, redirect

# Create your views here.
from group.forms import CreateGroupForm, JoinGroupForm
from group.models import Group
from account.models import Account
from django.contrib import messages


def group_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    group = user.belongs_to_group
    group_members = Account.objects.filter(belongs_to_group=group)
    context['members'] = group_members


    return render(request, 'group/group.html', context)

def create_group_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    form = CreateGroupForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = CreateGroupForm()
        return redirect('group:group_info')
    context['form'] = form
    return render(request, 'group/create_group.html', context)

def join_group_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    if request.POST:
        print("POST")
        print("is valid")
        try:      
            group_name = request.POST['belongs_to_group']
            group = Group.objects.get(name=group_name)
            print(group)
            user.belongs_to_group = group
            user.is_inTeam = True
            user.save()
            return redirect('group:group_info')
        except Group.DoesNotExist:
            messages.error(request, 'No such group') 


    return render(request, 'group/join_group.html', context)