from django.db import models

class UserMaster(models.Model):
    email = models.EmailField(max_length=50 ,null=True,blank=True)
    password = models.CharField(max_length=50 ,null=True,blank=True)
    otp = models.IntegerField()
    role = models.CharField(max_length=50 ,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

class candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50,null=True,blank=True)
    lastname = models.CharField(max_length=50,null=True,blank=True)
    contact = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    jobcatagory = models.CharField(max_length=50,null=True,blank=True)
    jobtype = models.CharField(max_length=50,null=True,blank=True)
    min_salary = models.IntegerField(null=True,blank=True)
    max_salary = models.IntegerField(null=True,blank=True)
    education_lavel = models.CharField(max_length=50,null=True,blank=True)
    experience = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    dob = models.CharField(max_length=50,null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True)
    
class company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50,null=True,blank=True)
    lastname = models.CharField(max_length=50,null=True,blank=True)
    company_name = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    contact = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=150,null=True,blank=True)
    logopic = models.ImageField(upload_to="img/companylogo")