from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from .encryption import *
from binascii import hexlify


def createUser(name, email, password):
    check = User.objects.filter(username=name).count()
    if check == 0:
        user = User.objects.create_user(name, email, password)
        user.save()
        return True
    else:
        return False


def checkCredentials(name, password):
    user = authenticate(username=name, password=password)
    if user is not None:
        return True
    else:
        return False


def addUserFromGroup(user, group):
    groupMembers = GroupMember.objects.all()
    for membership in groupMembers:
        if membership.username == user and membership.groupName == group:
            return  # already in group
    newMembership = GroupMember(username=user, groupName=group)
    newMembership.save()


def userInGroup(user, group):
    groupMembers = GroupMember.objects.all()
    for membership in groupMembers:
        if membership.username == user and membership.groupName == group:
            return True
    return False


def removeUserFromGroup(user, group):
    groupMembers = GroupMember.objects.all()
    for membership in groupMembers:
        if membership.username == user and membership.groupName == group:
            membership.delete()


def createGroup(groupName):
    privateKey = RSA.generate(1024)
    publicKey = privateKey.publickey()
    privateKeyString = privateKey.export_key().decode()
    publicKeyString = publicKey.export_key().decode()
    group = Group(groupName=groupName, publicKey=publicKeyString, privateKey=privateKeyString)
    group.save()


def deleteGroup(groupName):
    groups = Group.objects.all()
    for group in groups:
        if groupName in group.groupName:
            group.delete()
            connections = GroupMember.objects.all()
            for membership in connections:
                if membership.groupName in group.groupName:
                    membership.delete()


def postMessage(content, messageNumber, groupName, poster):
    group = Group.objects.get(groupName=groupName)
    publicKeyString = group.publicKey
    crypticContent = encrypt(publicKeyString, content)
    message = Message(content=crypticContent, messageNumber=messageNumber, groupName=groupName, poster=poster)
    message.save()


def deleteMessage(messageNumber):
    message = Message.objects.get(messageNumber=messageNumber)
    message.delete()