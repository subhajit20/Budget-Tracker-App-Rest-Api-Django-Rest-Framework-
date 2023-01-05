from django.db import models
from django.utils.timezone import now
from user.models import User

# Create your models here.
class Transaction(models.Model):
    transactionid = models.AutoField(primary_key=True,unique=True)
    category = models.CharField(max_length=100,editable=True)
    expensename = models.CharField(max_length=100,editable=True)
    cost = models.CharField(max_length=100,editable=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(default=now)

    @classmethod
    def Transact(cls,user,**krgs):
        if krgs and user:
            checkuser = User.objects.get(email=user)
            newtransaction = cls.objects.create(category=krgs["category"],expensename=krgs["expensename"],cost=krgs["cost"],user=checkuser)
            newtransaction.save()
            return True
        else:
            return False
    
    @classmethod
    def GetTransactions(cls,user):
        if user:
            checkuser = User.objects.get(email=user)
            alltransactions = cls.objects.filter(user=checkuser).values_list("category","expensename","cost","date")
            return {
                "status":True,
                "data":list(alltransactions)
            }
        else:
            return {
                "status":False,
            }
    @classmethod
    def GetTransactions_by_category(cls,user,cat):
        if user:
            checkuser = User.objects.get(email=user)
            alltransactions = cls.objects.filter(user=checkuser,category=cat).values_list("category","expensename","cost","date")
            return {
                "status":True,
                "data":list(alltransactions)
            }
        else:
            return {
                "status":False,
            }
    @classmethod
    def GetTransactions_by_date(cls,user,date):
        if user:
            checkuser = User.objects.get(email=user)
            alltransactions = cls.objects.filter(user=checkuser,date=date).values_list("category","expensename","cost","date")
            return {
                "status":True,
                "data":list(alltransactions)
            }
        else:
            return {
                "status":False,
            }