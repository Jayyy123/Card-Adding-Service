import email
from email.policy import default
from django.db import models
import uuid
from django.contrib.auth.models import User

class UserAccount(models.Model):

    sex = (
        ('male','MALE'),
        ('female','FEMALE'),
        ('other','OTHER'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False, null=False, default='user')
    last_name = models.CharField(max_length=100, blank=False, null=False, default='user')
    username = models.CharField(max_length=100, blank=False, null=False, default='user')
    email = models.EmailField()
    gender = models.CharField(choices=sex, default=sex[0][1], blank=False,null=False,max_length=100)
    profile_picture = models.ImageField(default='user.jpeg')
    date_of_birth = models.DateTimeField(default='2000-05-15', blank=False,null=False)
    bank_information = models.ManyToManyField('Bank')
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)


    def __str__(self) -> str:
        return self.username

class Bank(models.Model):

    type = (
        ('savings','SAVINGS'),
        ('current','CURRENT'),
        ('government','GOVERNTMENT'),
        ('motgage','MORTGAGE'),
        ('savings','STUDENT'),
        ('kids','KIDS'),
    )

    bank = (
        ('wema','WEMA'),
        ('access','ACCESS'),
        ('stanbic ibtc','STANBIC IBTC'),
        ('guaranty trust','GUARANTY TRUST'),
        ('first','FIRST'),
        ('united bank of Africa','UNITED BANK OF AFRICA'),
        ('other','OTHER'),
    )

    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    bank_name = models.CharField(choices=bank, default=bank[0][1],max_length=100)
    other = models.BooleanField(default=False)
    account_type = models.CharField(choices=type, default=type[0][1],max_length=100)
    account_number = models.PositiveBigIntegerField(default=0, blank=False,null=False)
    bvn = models.PositiveBigIntegerField(default=0, blank=False,null=False)

    
    def __str__(self) -> str:
        return self.bank_name

    

