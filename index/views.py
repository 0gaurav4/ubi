from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, reverse
from .models import Category,Services,cart,Order,video_lecture
from django.http import HttpResponse,JsonResponse

from django.conf import settings

# Create your views here.
def index(request):
    var=Category.objects.all().order_by("cat_name")
    return render(request,'index.html')

def about_us(request):
    return render(request,'about-us.html')
def profile(request):
    return render(request,'author-detail.html')
def authors(request):
    return render(request,'authors.html')
def service(request,cid):
    cat=Category.objects.get(id=cid)
    data=Services.objects.filter(cate=cat)
    return render(request,'service.html',{"data":data})

def search(request):
    if request.method=='GET':
        var2=request.GET["book"]
        data=Services.objects.filter(name__icontains=var2).order_by('name')
    return render(request,'service.html',{"data":data})

def service_1(request):
    
    data=Services.objects.all().order_by("cate")
    return render(request,'service.html',{"data":data})

def Cart(request):
    crt={}
    item=cart.objects.filter(user__id=request.user.id,status=False)
    crt["item"]=item
    if request.user.is_authenticated:
        if request.method=="POST":
            qty=request.POST["qty"]
            bid=request.POST["bid"]
            is_exist=cart.objects.filter(product__id=bid,user__id=request.user.id,status=False)
            if len(is_exist)>0:
                crt["messages"]="item already exist in cart"
            else:
                product=get_object_or_404(Services,id=bid)
                usr=get_object_or_404(User,id=request.user.id)
                c=cart(user=usr,product=product,qty=qty)
                c.save()
                crt["messages"]="{}item added in cart".format(product.name)
    else:
        crt["messages"]="Please login first"
    return render(request,"cart.html",crt)
    
def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
        return HttpResponse(cart_obj.quantity)

    if "delete_cart" in request.GET:
        id = request.GET["delete_cart"]
        cart_obj = get_object_or_404(cart,id=id)
        cart_obj.delete()
        return HttpResponse(1)

def get_cart_data(request):
    item=cart.objects.filter(user__id=request.user.id)
    sale,quantity=0,0
    for i in item:
        sale += float(i.cart.product.price)*i.quantity
        quantity += int(i.qty)
    res={"tot":sale,"quan":quantity}
    return JsonResponse(res)


def payment_done(request):
    if "order_id" in request.session:
        order_id = request.session["order_id"]
        ord_obj = get_object_or_404(Order,id=order_id)
        ord_obj.status=True
        ord_obj.save()
        
        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_object = cart.objects.get(id=i)
            cart_object.status=True
            cart_object.save()
    return render(request,"payment_success.html")

def payment_cancelled(request):
    return render(request,"payment_failed.html")

def video_l(request):
    video=video_lecture.objects.all()
    return render(request,"authors.html",{"video":video})