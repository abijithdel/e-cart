from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,login  as auth_login 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def login(req):
    if req.method == 'POST':
        uname = req.POST.get('username')
        pas = req.POST.get('password')
        user = authenticate(req,username=uname,password=pas)
        if user is not None:
            auth_login(req,user)
            
            return render(req,'index.html')
        else:
            us_pas_not_mach='Check Username or password'
            return render(req,'account/login.html',{'us_pas_not_mach':us_pas_not_mach})

    return render(req,'account/login.html')

def signup(req):
    if req.method == 'POST':
        fname = req.POST.get('firstname')
        lname = req.POST.get('lastname')
        uname = req.POST.get('username')
        email = req.POST.get('email')
        pass1 = req.POST.get('password')
        pass2 = req.POST.get('cpassword')
        
        if pass1 != pass2:
            pass_not_mach='Check Confirm Password'
            return render(req,'account/signup.html',{'pass_not_mach':pass_not_mach})
        

        elif User.objects.filter(username=uname).exists():
            username_taken = 'Username already taken'
            return render(req, 'account/signup.html', {'username_taken': username_taken})
        else:
            users = User.objects.create_user(username=uname, email=email, password=pass1, first_name=fname, last_name=lname)
            users.save()
            wel_mess='Welcome',fname,'Login Now'
            return render(req,'account/login.html',{'wel_mess':wel_mess})
            
    return render(req,'account/signup.html')



def account(req):
    return render(req,'account/account.html')


def edit_profile(req):
    user = req.user
    if req.method == 'POST':
        user.first_name = req.POST.get('first_name')
        user.last_name = req.POST.get('last_name')
        user.username = req.POST.get('username')
        user.email = req.POST.get('email')
        user.save()
        saccessf = 'Profile saccessfully Edited'
        return render(req, 'account/account.html', {'user': user , "saccess":saccessf})
    else:
        pass
    return render(req, 'account/account-ed.html', {'user': user})


def reset_pass(req):
    user = req.user
    if req.method == 'POST':
        pass1 = req.POST.get('newpass')
        pass2 = req.POST.get('cpass')
        if pass1 != pass2:
            response ="Check Conform Password"
            return render(req,'account/pass-change.html',{'response':response})

        else:
          user.set_password(pass1)
          update_session_auth_hash(req, user)
          user.save()
          responses = "Password Changed"
          return render(req,'account/account.html',{'responses':responses})
    return render(req,'account/pass-change.html')


def delete_accout_user(req):
    if req.method == 'POST':
        user = req.user
        user.delete()
        alert = 'Your Accout Deleted'
        return render(req,'account/signup.html',{'alert':alert})
    return render(req,'account/delete_account.html')
