from django.db import models

# Create your models here.
class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'note'

class Register(models.Model):
    register_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'register'

class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'