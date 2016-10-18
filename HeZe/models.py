from django.db import models

# Create your models here.

class User(models.Model):
    UserId = models.IntegerField(primary_key=True)
    PassWord = models.CharField(max_length=255)
    TrueName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    UserPhone = models.CharField(max_length=255)
    Label1 = models.CharField(max_length=255)
    Label2 = models.CharField(max_length=255)
    Label3 = models.CharField(max_length=255)

class SendHezu(models.Model):
    SendHezuId = models.IntegerField(primary_key=True)
    UserId = models.IntegerField(max_length=11)
    Information = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Picture = models.CharField(max_length=255)
    Number = models.IntegerField(max_length=11)
    Delete = models.IntegerField(max_length=11)


class Circle(models.Model):
    CircleId = models.IntegerField(primary_key=True)
    UserId = models.IntegerField(max_length=11)
    Information = models.CharField(max_length=255)
    Picture = models.CharField(max_length=255)


class CircleComment(models.Model):
    CommentId = models.IntegerField(primary_key=True)
    CircleId = models.IntegerField(max_length=11)
    UserId = models.IntegerField(max_length=11)
    Comment = models.CharField(max_length=255)


class Label(models.Model):
    LabelId = models.IntegerField(primary_key=True)
    Label = models.IntegerField(max_length=11)


class CheckCode(models.Model):
    CheckCodeId = models.IntegerField(primary_key=True)
    UserPhone = models.CharField(max_length=255)
    CheckCode = models.CharField(max_length=255)

