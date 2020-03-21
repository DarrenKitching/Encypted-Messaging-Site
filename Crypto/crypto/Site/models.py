from django.db import models


class GroupMember(models.Model):
    username = models.CharField(max_length=50)
    groupName = models.CharField(max_length=50)


class Message(models.Model):
    content = models.BinaryField() # change message save to ByteField
    messageNumber = models.PositiveIntegerField()
    groupName = models.CharField(max_length=50)
    poster = models.CharField(max_length=50)


class Group(models.Model):
    groupName = models.CharField(max_length=50)
    publicKey = models.CharField(max_length=10000)
    privateKey = models.CharField(max_length=10000)


class Control(models.Model):
    messageCounter = models.PositiveIntegerField()
