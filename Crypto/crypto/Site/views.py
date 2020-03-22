from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from . import system
from . import models


def index(request):
    return render(request, 'login.html')


def submit(request):
    name = str(request.POST.get('uname'))
    password = str(request.POST.get('psw'))
    request.session['name'] = name
    request.session['password'] = password
    if system.checkCredentials(name, password):
        return HttpResponseRedirect('home')
    else:
        return HttpResponseRedirect('badcredentials')


def badcredentials(request):
    template = loader.get_template('badcredentials.html')
    return HttpResponse(template.render())


def home(request):
    allmygroups = models.GroupMember.objects.all()
    allExistingGroups = models.Group.objects.all()
    users = User.objects.all()
    mygroups = []
    allGroups = []
    userList = []
    for group in allmygroups:
        if group.username == request.session['name']:
            print(group.groupName)
            mygroups.append(group.groupName)
    for group in allExistingGroups:
        allGroups.append(group.groupName)
    for user in users:
        userList.append(user.username)
    context = {
        'groups': mygroups,
        'allGroups': allGroups,
        'users': userList,
    }
    return render(request, 'home.html', context)


def createuser(request):
    return render(request, 'create.html')


def submitcreate(request):
    name = str(request.POST.get('uname'))
    password = str(request.POST.get('psw'))
    request.session['name'] = name
    request.session['password'] = password
    attempt = system.createUser(name, None, password)
    if attempt:
        return HttpResponseRedirect('home')
    else:
        return HttpResponseRedirect('badcredentials')


def post(request):
    message = request.GET['message']
    postGroup = request.GET['postGroup']
    control = models.Control.objects.all()
    control[0].messageCounter += 1
    control[0].save()
    counter = control[0].messageCounter
    system.postMessage(message.encode(), counter, postGroup, request.session['name'])
    return HttpResponseRedirect('messages')


def add(request):
    user = request.GET['addUser']
    group = request.GET['addGroup']
    system.addUserFromGroup(user, group)
    return HttpResponseRedirect('home')


def remove(request):
    user = request.GET['removeUser']
    group = request.GET['removeGroup']
    system.removeUserFromGroup(user, group)
    return HttpResponseRedirect('home')


def create(request):
    groupName = request.GET['createGroup']
    system.createGroup(groupName)
    return HttpResponseRedirect('home')


def delete(request):
    groupName = request.GET['deleteGroup']
    system.deleteGroup(groupName)
    return HttpResponseRedirect('home')


def messages(request):
    allMessages = models.Message.objects.all()
    for message in allMessages:
        if system.userInGroup(request.session['name'], message.groupName):
            group = models.Group.objects.get(groupName=message.groupName)
            privateKeyString = group.privateKey
            decoded = system.decrypt(privateKeyString, message.content).decode()
            message.content = decoded
    context = {
        'allMessages': allMessages,
    }
    return render(request, 'messages.html', context)
