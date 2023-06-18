from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import profile

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about-us.html")
def authordetail(request):
    return render(request,"author-detail.html")
def authors(request):
    return render(request,"authors.html")
def blogdetail(request):
    return render(request,"blog-detail.html")
def blogfull(request):
    return render(request,"blog-full.html")
def blog(request):
    return render(request,"blog.html")
def bookdetail(request):
    return render(request,"book-detail.html")
def blside1(request):
    return render(request,"book-listing-1-w-sidebar.html")
def blisting(request):
    return render(request,"book-listing-1.html")
def blside2(request):
    return render(request,"book-listing-2-w-sidebar.html")
def cart(request):
    return render(request,"cart.html")
def contact(request):
    return render(request,"contact.html")
def service(request):
    return render(request,"service.html")
def payfailed(request):
    return render(request,"payment_failed.html")
def paysucess(request):
    return render(request,"payment_sucess.html")
def processpay(request):
    return render(request,"process_payment.html")
def register(request):
    if request.method=="POST":
        finame=request.POST["fname"]
        ln=request.POST["lname"]
        mail=request.POST["email"]
        un=request.POST["uname"]
        cno=request.POST["cn"]
        password=request.POST["pass"]
        confirmpass=request.POST["cpass"]

        if password==confirmpass:
            if User.objects.filter(username=un).exists():
                messages.info(request,"Userrname already exist")
                messages.info(request,un)
                return redirect("register")
            else:
                user=User.objects.create_user(username=un,first_name=finame,last_name=ln,email=mail,password=password)
                user.save()
                user2 = profile(user=user, contact=cno)
                user2.save()
                return redirect("login")
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        un=request.POST["uname"]
        password=request.POST["pass"]
        au=auth.authenticate(username=un,password=password)
        if au is not None:
            auth.login(request,au)
            return redirect("index")
            
        else:
            return redirect("login")
            
    return render(request,"login.html")


def logout(request):

    auth.logout(request)
    return redirect("index")

def cprofile(request):
    display = {}
    prof = profile.objects.filter(user__id=request.user.id)
    if len(prof)>0:
        prfd=profile.objects.get(user__id=request.user.id)
        display["prodisplay"]=prfd
        
    return render(request, "profile.html",display)

def update(request):
    display = {}
    prof = profile.objects.filter(user__id=request.user.id)
    if len(prof)>0:
        prfd=profile.objects.get(user__id=request.user.id)
        display["prodisplay"]=prfd
        if request.method=='POST':
            fn=request.POST["fname"]
            ln=request.POST["ln"]
            un=request.POST["uname"]
            em=request.POST["email"]
            #clid=request.POST["collegid"]
            cno=request.POST["phn"]
            
            ad=request.POST["address"]
            city=request.POST["city"]
            state=request.POST["state"]
            pin=request.POST["pincode"]
            
            
            user=User.objects.get(id=request.user.id)
            user.first_name=fn
            user.last_name=ln
            user.email=em
            user.uname=un
            user.save()
            prfd.conatct_number=cno
            #prfd.collegeid=clid
            prfd.address=ad
            prfd.city=city
            prfd.state=state
            prfd.pincode=pin
            prfd.save()
            if "img" in request.FILES:
                pic=request.FILES["img"]
                prfd.ppic=pic
                prfd.save()
            return redirect("profile")
    return render(request, "update.html",display)
    
