from django.db import models

class Attribute(models.Model):
    user = models.OneToOneField('auth.User', related_name='attr',on_delete=models.CASCADE)
    attend_no = models.CharField(max_length=20)
    phonetic = models.CharField(max_length=30)
    org_name = models.CharField(max_length=50)
    team = models.ForeignKey('Team', related_name='member', on_delete=models.SET_NULL,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class Team(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)





