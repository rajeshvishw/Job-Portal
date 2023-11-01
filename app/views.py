from django.shortcuts import render
from .models import *
from random import randint
from django.shortcuts import redirect

def homeView(request):
    return render(request,"index.html")

def signupView(request):
    return render(request,"signup.html")

def register(request):
    if request.POST['userType'] == "Candidate":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        role = request.POST['userType']
       
        user = UserMaster.objects.filter( email = email )
        if user:
            massage = "user alrady exist"
            return render(request,"signup.html",{"massage":massage})
        else:
            if password == confirmPassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role = role, otp = otp, email = email, password = password)
                candidate.objects.create(user_id = newuser, firstname = firstName, lastname = lastName)
                return render(request,"otpveryfy.html",{"email":email,"name":firstName})
    else:
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        role = request.POST['userType']
       
        user = UserMaster.objects.filter( email = email )
        if user:
            massage = "user alrady exist"
            return render(request,"signup.html",{"massage":massage})
        else:
            if password == confirmPassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role = role, otp = otp, email = email, password = password)
                company.objects.create(user_id = newuser, firstname = firstName, lastname = lastName)
                return render(request,"otpveryfy.html",{"email":email,"name":firstName})

def otpveryfyView(request):
    email = request.POST['email']   
    otp = request.POST['otp']
    checkemail = UserMaster.objects.get(email= email)
    if checkemail.role == "Candidate":
        email = candidate.objects.get(user_id = checkemail)
        name = email.firstname
        if checkemail:
            otpcheck = UserMaster.objects.filter(otp=otp)
            if otpcheck:
                return render(request,"index.html",{"name":name})
            else:
                massage = "Invalid OTP"
                return render(request,"otpveryfy.html",{"massage":massage})
        else:
            return render(request,"signup.html")
    else:
        email = company.objects.get(user_id = checkemail)
        name = email.firstname+email.lastname
        
        if checkemail:
            otpcheck = UserMaster.objects.filter(otp=otp)
            if otpcheck:
                return render(request,"company/index.html")
            else:
                massage = "Invalid OTP"
                return render(request,"otpveryfy.html",{"massage":massage})
        # else:
        #     return render(request,"company/index.html")
        
        
def login(request):
    if request.method == "POST":
        role = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']
        if role == "Candidate":
            check = UserMaster.objects.get(email = email)
            if check:
                try:
                    passwordcheck = UserMaster.objects.get(password=password)
                # if passwordcheck:   
                    get_candidate_name = candidate.objects.get(user_id = check)  
                    firstname = get_candidate_name.firstname
                    lastname = get_candidate_name.lastname
                    request.session['id'] = check.id
                    request.session['role'] = check.role
                    request.session['email'] = check.email  
                    request.session['firstname'] = firstname
                    request.session['lastname'] = lastname
                    return render(request,"index.html")
                # else:
                except:
                    massage = "Username and password wrong"
                    return render(request,"login.html",{"massage":massage})
            else:
                massage = "Username and password wrong"
                return render(request,"login.html",{"massage":massage})
        else:
            check = UserMaster.objects.get(email = email)
            if check:
                try:
                    passwordcheck = UserMaster.objects.get(password=password)
                # if passwordcheck:   
                    get_candidate_name = company.objects.get(user_id = check)  
                    firstname = get_candidate_name.firstname
                    lastname = get_candidate_name.lastname
                    request.session['id'] = check.id
                    request.session['role'] = check.role
                    request.session['email'] = check.email  
                    request.session['firstname'] = firstname
                    request.session['lastname'] = lastname
                    return render(request,"company/index.html",{"name":firstname+lastname})
                # else:
                except:
                    massage = "Username and password wrong"
                    return render(request,"login.html",{"massage":massage})
            else:
                massage = "Username and password wrong"
                return render(request,"login.html",{"massage":massage})
            
    return render(request,"login.html")


def profile(request,pk):
    usergetdata = UserMaster.objects.get(pk=pk)
    candidategetdata = candidate.objects.get(user_id = usergetdata)
    email = usergetdata.email
    firstname = candidategetdata.firstname
    lastname = candidategetdata.lastname
    image = candidategetdata.profile_pic if candidategetdata.profile_pic!='' else ''
    print(image,"iiiiiiiiiiiiiiiiiiii")
    return render(request,"profile.html",{"email":email,"firstname":firstname,"lastname":lastname,"image":image})

def updateProfile(request,pk):
    checkmuser = UserMaster.objects.get(pk=pk)
    if checkmuser:
        candidatecheck = candidate.objects.get(user_id = checkmuser)
        candidatecheck.firstname = request.POST['firstName']
        candidatecheck.lastname = request.POST['lastName']
        candidatecheck.city = request.POST['city']
        candidatecheck.country = request.POST['country']
        candidatecheck.jobcatagory = request.POST['jobCategory']
        candidatecheck.jobtype = request.POST['jobType']
        candidatecheck.min_salary = request.POST['minSalary'] if request.POST['minSalary'] !="" else 0
        candidatecheck.education_lavel = request.POST['educationLevel']
        candidatecheck.experience = request.POST['experience']
        try:
            candidatecheck.profile_pic = request.FILES['image']
        except:
            pass
        candidatecheck.save()
        # formating url
        url = f'/profile/{pk}/'# isme profile url name se liya gaya hai
        return redirect(url)
        
#======================== COMPANY ===========================
def companyView(request,pk):
    print(pk)
    return render(request,"company/index.html")

def profileView(request,pk):
    getdata = UserMaster.objects.get(id=pk)
    companydata = company.objects.get(user_id = getdata)
    firstname = companydata.firstname
    lastname = companydata.lastname
    company_name = companydata.company_name
    state = companydata.state
    city = companydata.city
    contact = companydata.contact
    address = companydata.address
    logopic = companydata.logopic
    return render(request,"company/profile.html",{"firstname":firstname,"lastname":lastname,"company_name":company_name,"state":state,"city":city,"contact":contact,"address":address,"logopic":logopic})

def profileupdateView(request,pk):
    getuser = UserMaster.objects.get(pk=pk)
    candidatedata = company.objects.get(pk=getuser)
    print(request.POST['firstname'])
    return render(request,company/profile.html)