from django.db import models

# Create your models here.

class User(models.Model):
    UserId = models.IntegerField(primary_key=True)
    PassWord = models.CharField(max_length=255)
    UserPhoto = models.CharField(max_length=255)
    NickName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    UserPhone = models.CharField(max_length=255)
    Label1 = models.CharField(max_length=255)
    Label2 = models.CharField(max_length=255)
    Label3 = models.CharField(max_length=255)
    SecretKey = models.CharField(max_length=255)
    Token = models.CharField(max_length=255)
    Lon_Lat = models.CharField(max_length=255)


class SendHezu(models.Model):
    SendHezuId = models.IntegerField(primary_key=True)
    UserId = models.IntegerField()
    Information = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Picture = models.CharField(max_length=255)
    Number = models.IntegerField()
    Delete = models.IntegerField()
    Label1 = models.CharField(max_length=255)
    Label2 = models.CharField(max_length=255)
    Distance = models.IntegerField()
    Lon_Lat = models.CharField(max_length=255)


class Circle(models.Model):
    CircleId = models.IntegerField(primary_key=True)
    UserId = models.IntegerField()
    Information = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    Picture1 = models.CharField(max_length=255)
    Picture2 = models.CharField(max_length=255)
    Picture3 = models.CharField(max_length=255)
    Picture4 = models.CharField(max_length=255)
    Picture5 = models.CharField(max_length=255)
    Picture6 = models.CharField(max_length=255)
    Picture7 = models.CharField(max_length=255)
    Picture8 = models.CharField(max_length=255)
    Picture9 = models.CharField(max_length=255)

class CircleComment(models.Model):
    CommentId = models.IntegerField(primary_key=True)
    CircleId = models.IntegerField()
    UserId = models.IntegerField()
    Comment = models.CharField(max_length=255)


class Label(models.Model):
    LabelId = models.IntegerField(primary_key=True)
    Label = models.IntegerField()


class Checkcode(models.Model):
    CheckCodeId = models.IntegerField(primary_key=True)
    UserPhone = models.CharField(max_length=255)
    CheckCode = models.CharField(max_length=255)
    SendTime = models.DateTimeField()


class Attention(models.Model):
    AttentionId = models.IntegerField(primary_key=True)
    UserId = models.IntegerField()
    BefocusonId = models.IntegerField()

