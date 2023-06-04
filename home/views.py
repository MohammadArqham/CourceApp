from itertools import count, product
from multiprocessing.dummy import current_process
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
import json
from django.contrib.auth import authenticate, login


def computeCart(items):
    count = 0
    price = 0

    for i in items:
        count += 1
        price += i.cource.price
    
    return {'count':count,'price':price}

def home(request):
    a = models.Cource.objects.all()
    i=''
    print("_________________________________________________")
    
    if request.user.is_authenticated:
        i=models.cource_user.objects.get(user=request.user) 
    return render(request,'index.html',{'cources':a,'img':i})


def user_login(request):
    return render(request,'login.html')

def login_data(request):
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(request,username=username, password=password)
    if user is not None:
        login(request,user)
       
        return redirect('../../')
    else:
        print('error')
        return HttpResponse('error')

def logout_data(request):
    logout(request)
    return redirect('../')

def signup(request):
    return render(request,'signup.html')

def signdata(request):
    print("this is the text #####################################################################")
    print(request.POST) 
    username1 = request.POST['username']
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST['email']
    pswd = request.POST['password']
    ######################################################

    dis = request.POST.get('discription')
    d_dis = request.POST.get('detiled_discription')
    img =request.FILES.get('image') 
    cat =request.POST.get('category') 

    a = User.objects.create_user(username=username1,first_name=fname,last_name =lname, email = email, password = pswd )  
    a.save()
    try:
        user = authenticate(request,username=username1, password=pswd)
        login(request,user)
       
        
    except:
        print('error')
        return HttpResponse(f'error{user}')


    u_user = User.objects.get(username=username1)

    b = models.cource_user.objects.create(user=u_user, type=cat, image= img, des=dis, detailed_discription=d_dis, experience = 0, rating = 0.0)
    print(b)
    
    return redirect('../../')
    
    
  
def profile(request):
    try:
        p = models.cource_user.objects.get(user=request.user)

        cur = models.Cource.objects.filter(author = p)
        return render(request, 'profile.html',{'profile':p,'cources':cur})
    except:

        return user_login(request)

def addCource_form(request):
    return render(request,'add_cource.html')

def addCource(request):
    print("####################################################")
    print(request.POST)
    aut = User.objects.get(username = request.user)
    pro = models.cource_user.objects.get(user=aut)

    models.Cource.objects.create(author=pro,name=request.POST.get('name'),des=request.POST.get('dis'),price=request.POST.get('price'),duration = 0, image=request.FILES.get('image'),rating = 0.0,detailed_discription=request.POST.get('detailed_dis'),preview_video=request.POST.get('vedio'),pdf=request.POST.get('pdf'),category=request.POST.get('category'),bought=0,impresions=0,clicks=0 )
    return redirect('../')


def cartPage(request):
    cuurentuser = models.cource_user.objects.get(user = request.user)
    print("####################################################")
    cart = models.cart.objects.filter(name=cuurentuser)
    cartData = computeCart(cart)

    return render(request, 'cart.html',{'cart':cart, 'cartData':cartData})

def myCources(request):
    cuurentuser = models.cource_user.objects.get(user = request.user)
    print("####################################################")
    cources = models.my_cources.objects.filter(name=cuurentuser)
    return render(request,'my-cources.html',{'cources':cources})

def showCource(request,pk):
    product = models.Cource.objects.get(id = pk)
    comments = models.comment.objects.filter(cource = product)
    
    return render(request,'product.html',{'product':product,'comments':comments})

def shippingpage(request,pk):
    return render(request,'shipping.html')

def shipping(request,pk):
    c_user = models.cource_user.objects.get(user=request.user)
    cource = models.Cource.objects.get(id = pk)
    models.my_cources.objects.create(name = c_user,cource = cource)
    return redirect('/')


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def addCart(request):
    data = json.loads(request.body)
    print("========================================")
    print(data)
    action = data['Action']
    print(action)
    c_user = models.cource_user.objects.get(user=request.user)
    if request.user.is_authenticated:
        if 'add' in action:
            cource = models.Cource.objects.get(id = data['idno'])
            cartdata = models.cart.objects.get_or_create(name = c_user,cource = cource )
        
        else:
            cartitem = models.cart.objects.get(id = data['idno'])
            cartitem.delete()
        return HttpResponse(request,'confirm')
    
    return JsonResponse('unauthorised')

@csrf_exempt   
def addComment(request,pk):
    data = json.loads(request.body)
    c_user = models.cource_user.objects.get(user=request.user)
    cource = models.Cource.objects.get(id = pk)
    a = models.comment.objects.create(name = c_user,cource = cource,comment =data['Data'] )
    a.save()


def licensing(request):
    return render(request,'licensing.html')
