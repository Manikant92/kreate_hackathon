from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

DOCTYPE_CHOICES = (
        ('PAN', 'PAN Card,'),
        ('AADHAR', 'Aadhar Card'),
        ('DRIVINGLICENCE', 'Driving License'),
        ('VOTERID', 'Voter ID'),
        ('BANKSTATEMENT', 'Bank Statements'),
    )


class CustomerData(models.Model):
    cust_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True,null=True)
    father_name = models.CharField(max_length=100,blank=True,null=True)
    dob = models.CharField(blank=True,null=True,max_length=20)
    address = models.TextField(blank=True,null=True)
    doc_type = models.CharField(choices=DOCTYPE_CHOICES, blank=True,max_length=100)
    doc_id = models.CharField(blank=True,null=True,max_length=100)
    created = models.DateTimeField(auto_now_add=True)




class NameMatch(models.Model):
    cust_id=models.CharField(max_length=100,unique=True)
    cosine_percentage=models.CharField(max_length=100)
    reorder_flg=models.BooleanField(default=False)


class DOBMatch(models.Model):
    cust_id=models.CharField(max_length=100,unique=True)
    dob_flg=models.BooleanField(default=False)
    year_flg=models.BooleanField(default=False)


# class AccuracyDetails(models.Model):
#     customer_id = models.CharField(max_length=100)
#     doc_type1 = models.CharField(choices=DOCTYPE_CHOICES, blank=True,max_length=100)
#     doc_type2 = models.CharField(choices=DOCTYPE_CHOICES, blank=True,max_length=100)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     father_name = models.CharField(max_length=100, blank=True, null=True)
#     dob = models.CharField(blank=True, null=True, max_length=20)
#     address = models.TextField(blank=True, null=True)
#     doc_id = models.CharField(blank=True, null=True, max_length=100)
#     created = models.DateTimeField(auto_now_add=True)



