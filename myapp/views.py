from django.shortcuts import render,redirect
from django.contrib import messages
from .models import*
from django.db.models import Q
import re
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method == "POST":
        studentPassword = request.POST.get("studentPassword")
        ConfirmPassword = request.POST.get("ConfirmPassword")
        if studentPassword == ConfirmPassword:
            FirstName = request.POST.get('FirstName')
            LastName = request.POST.get("LastName")
            RollNo = request.POST.get("RollNo")
            PhoneNumber = request.POST.get("PhoneNumber")
            studentEmail = request.POST.get("studentEmail")   
            email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
            if not email_pattern.match(studentEmail):
                messages.error(request, "Please enter a valid email address")
                return render(request, 'register.html')
            phone_pattern = re.compile(r'^\d{10}$')  
            if not phone_pattern.match(PhoneNumber):
                messages.error(request, "Please enter a valid phone number")
                return render(request, 'register.html')

            customer = Student.objects.create(FirstName=FirstName, LastName=LastName, RollNo=RollNo, PhoneNumber=PhoneNumber, studentEmail=studentEmail, studentPassword=studentPassword, ConfirmPassword=ConfirmPassword)
            if customer:
                messages.success(request, "User profile has been registered successfully! Please login to continue")
                return redirect('user_login')
        else:
            messages.error(request, "Passwords do not match! Please try again")
    
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        RollNo = request.POST.get('RollNo')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(RollNo=RollNo, studentPassword=password)
            if student.status == 'Approved':
                request.session['RollNo'] = student.RollNo
                request.session['user_id'] = student.id
                return redirect('dashboard')  
            else:
                messages.error(request, "Your account has not been approved yet.")
                return redirect('user_login')
        except Student.DoesNotExist:
            messages.error(request, 'Invalid RollNo or password.')
            return render(request, 'login.html')
    elif 'RollNo' in request.session:
        return redirect('dashboard')  # Redirect if the user is already logged in
    else:
        return render(request, 'login.html')

def user_logout(request):
    if 'RollNo' in request.session:
        del request.session['RollNo']
    return redirect('user_login')

def edit_users(request):
    user_id=request.session['user_id']    
    useredit=Student.objects.get(id=int(user_id))
    password = useredit.ConfirmPassword

    if request.method == 'POST':
        OldPassword = request.POST.get("OldPassword")        
        if OldPassword != password:
            messages.error(request, 'Invalid old Password! Please Try Again')
        else:
            FirstName = request.POST.get("FirstName")
            LastName = request.POST.get("LastName")
            RollNo = request.POST.get("RollNo")
            PhoneNumber = request.POST.get("PhoneNumber")
            studentEmail = request.POST.get("studentEmail")
            studentPassword = request.POST.get("studentPassword")
            ConfirmPassword = request.POST.get("ConfirmPassword")
            
            if studentPassword == ConfirmPassword:
                # Update user fields and save
                useredit.FirstName = FirstName
                useredit.LastName = LastName
                useredit.RollNo = RollNo
                useredit.PhoneNumber = PhoneNumber
                useredit.studentEmail = studentEmail
                useredit.studentPassword = studentPassword
                useredit.ConfirmPassword = ConfirmPassword
                useredit.save()
                
                messages.success(request, "User profile has been updated successfully! Please to continue shopping")
                return redirect('user_logout')
            else:
                messages.error(request, "The password and confirmation do not match")

    return render(request, 'profile.html', {'useredit': useredit})

def clgComp(request):
    user_id=request.session['user_id']
    uid=Student.objects.get(id=int(user_id))
    if request.method == "POST":
        issuetype = request.POST.get('issuetype')
        location = request.POST.get('location')
        issue = request.POST.get('issue')
        impact = request.POST.get('impact')
        cmp = CollegeGrievance.objects.create(student=uid,
         IssueType=issuetype,Location=location,Issue=issue,
         Impact=impact)
        if cmp:
            messages.success(request,'Your Complaint has been submitted Successfully')
            return redirect('vcollege')
        else:
            messages.warning(request,"Error in Submitting your complaint") 
    
    return render(request,'collegecomplain.html')

def hosComp(request):
    user_id=request.session['user_id']
    uid=Student.objects.get(id=int(user_id))
    if request.method == "POST":
        issuetype = request.POST.get('issuetype')
        location = request.POST.get('location')
        issue = request.POST.get('issue')
        impact = request.POST.get('impact')
        cmp = HostelGrievance.objects.create(student=uid,
         IssueType=issuetype,RoomNumber=location,Issue=issue,
         Impact=impact)
        if cmp:
            messages.success(request,'Your Complaint has been submitted Successfully')
            return redirect('vhostel')
        else:
            messages.warning(request,"Error in Submitting your complaint") 
    
    return render(request,'hostelcomplain.html')

def cons(request):
    user_id=request.session['user_id']
    uid=Student.objects.get(id=int(user_id))

    context = {
        'CATEGORY_CHOICES': Counseling.CATEGORY_CHOICES
    }

    if request.method == "POST":
        category = request.POST.get('category')
        issue = request.POST.get('issue')
        cmp = Counseling.objects.create(student=uid,
         category=category,Problem=issue)
        if cmp:
            messages.success(request,'Your request has been submitted Successfully')
            return redirect('vcons')
        else:
            messages.warning(request,"Error in Submitting your request") 
    
    return render(request,'counseling.html',context)

def creti(request):
    user_id=request.session['user_id']
    uid=Student.objects.get(id=int(user_id))
    if request.method == "POST":
        cname = request.POST.get('cname')
        Purpose = request.POST.get('Purpose')        
        cmp = Certificate.objects.create(student=uid,
         certificate_type=cname,Purpose=cname)
        if cmp:
            messages.success(request,'Your request has been submitted Successfully')
            return redirect('vcerti')
        else:
            messages.warning(request,"Error in Submitting your request")  
    return render(request,'certificate.html')

def vcollege(request):
    user_id=request.session['user_id']
    uid=Student.objects.get(id=int(user_id))
    cmp = CollegeGrievance.objects.filter(student=uid)
    context={
        'cmp':cmp
    }
    return render(request,'viewcomp.html',context)

def vhostel(request):
    user_id=request.session['user_id']
    uid=Student.objects.get(id=int(user_id))
    hmp = HostelGrievance.objects.filter(student=uid)
    context={
        'hmp':hmp
    }
    return render(request,'vhoscomp.html',context)

def vcons(request):
    user_id=request.session['user_id']
    uid=Student.objects.get(id=int(user_id))
    hmp = Counseling.objects.filter(student=uid)
    context={
        'hmp':hmp
    }
    return render(request,'vcons.html',context)

def vcerti(request):
    user_id=request.session['user_id']
    uid=Student.objects.get(id=int(user_id))
    hmp = Certificate.objects.filter(student=uid)
    context={
        'hmp':hmp
    }
    return render(request,'vcerti.html',context)

def staff_login(request):
    if request.method == 'POST':
        staffId = request.POST.get('RollNo')
        password = request.POST.get('password')
        student = staff.objects.get(staffId=staffId, password=password)   
        if student:         
            request.session['staffId'] = student.staffId
            request.session['staffId'] = student.id
            return redirect('dashboard')             
        else:
            messages.error(request, 'Invalid staff Id or password.')
            return render(request, 'login.html')
    elif 'staffId' in request.session:
        return redirect('dashboard')  # Redirect if the user is already logged in
    else:
        return render(request, 'login.html')

def staff_logout(request):
    if 'staffId' in request.session:
        del request.session['staffId']
    return redirect('staff_login')

def dclg(request):
    cmp = CollegeGrievance.objects.all()
    context={
        'cmp':cmp,
        'STATUS_CHOICES' : CollegeGrievance.STATUS_CHOICES
    }
    if request.method == "POST":
        status = request.POST.get('status')
        clg = CollegeGrievance.objects.update(status=status)
        if clg:
            messages.success(request,"Complaint Updated Successfully")
            return redirect("dclg")
        else:
            messages.warning(request,"Error Updating Complaint")
            return redirect("dclg")
    return render(request,'dclg.html',context)

def dhos(request):
    cmp = HostelGrievance.objects.all()
    context={
        'cmp':cmp,
        'STATUS_CHOICES' : HostelGrievance.STATUS_CHOICES
    }
    if request.method == "POST":
        status = request.POST.get('status')
        clg = HostelGrievance.objects.update(status=status)
        if clg:
            messages.success(request,"Complaint Updated Successfully")
            return redirect("dhos")
        else:
            messages.warning(request,"Error Updating Complaint")
            return redirect("dhos")
    return render(request,'dhos.html',context)

def dcons(request):
    cmp = Counseling.objects.all()
    context={
        'cmp':cmp,
        'STATUS_CHOICES' : Counseling.STATUS_CHOICES
    }
    if request.method == "POST":
        status = request.POST.get('status')
        clg = Counseling.objects.update(status=status)
        if clg:
            messages.success(request,"Complaint Updated Successfully")
            return redirect("dcons")
        else:
            messages.warning(request,"Error Updating Complaint")
            return redirect("dcons")
    return render(request,'dcons.html',context)
    
def dcerti(request):
    cmp = Certificate.objects.all()
    context={
        'cmp':cmp,
        'STATUS_CHOICES' : Certificate.STATUS_CHOICES
    }
    if request.method == "POST":
        status = request.POST.get('status')
        clg = Certificate.objects.update(status=status)
        if clg:
            messages.success(request,"Complaint Updated Successfully")
            return redirect("dcerti")
        else:
            messages.warning(request,"Error Updating Complaint")
            return redirect("dcerti")
    return render(request,'dcerti.html',context)


        




