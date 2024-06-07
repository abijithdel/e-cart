from django.shortcuts import render
from django.contrib.auth import authenticate,login  as auth_login 

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
            return render(req,'account/index.html',{'us_pas_not_mach':us_pas_not_mach})

    return render(req,'account/login.html')