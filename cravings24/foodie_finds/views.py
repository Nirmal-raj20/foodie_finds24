from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages
from foodie_finds.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout
import json

# Create your views here.
def home(request):
    products=Products.objects.filter(trending=1)
    return render(request,'foodie_finds/index.html',{"products":products})

def bag_page(request):
  if request.user.is_authenticated:
    bag=Bag.objects.filter(user=request.user)
    return render(request,"foodie_finds/bag.html",{"bag":bag})
  else:
    return redirect("/")
 
def remove_bag(request,cid):
  bagitem=Bag.objects.get(id=cid)
  bagitem.delete()
  return redirect("/bag") 

def add_to_bag(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      #print(request.user.id)
      product_status=Products.objects.get(id=product_id)
      if product_status:
        if Bag.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Bag'}, status=200)
        else:
          if product_status.status==0:
            Bag.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Bag'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Bag'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
     if request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"logged in successfully")
            return redirect("/")
        else:
            messages.error(request,"invalid user name or password")
            return redirect("/login")
    return render(request,"foodie_finds/login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out successfully")
    return redirect("/")

def reg(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration successful you can login now...!")
            return redirect('/login')
    return render(request,'foodie_finds/register.html',{'form':form})

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,'foodie_finds/collections.html',{"catagory":catagory})

def collectionsview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        products=Products.objects.filter(catagory__name=name)
        return render(request,'foodie_finds/products/index.html',{"products":products,"category_name":name})
    else:
        messages.warning(request,"product is not available")
        return redirect(request,"out of stock")

def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname)):
        if(Products.objects.filter(name=pname)):
            products=Products.objects.filter(name=pname).first()
            return render(request,"foodie_finds/products/product_details.html",{"products":products})
        else:
            messages.error(request,"no such catagory found")
            return redirect('collections')
    else:
        messages.error(request,"no such catagory found")
        return redirect('collections')
    
def favviewpage(request):
  if request.user.is_authenticated:
    fav=Favourite.objects.filter(user=request.user)
    return render(request,"foodie_finds/fav.html",{"fav":fav})
  else:
    return redirect("/")
 
def remove_fav(request,fid):
  item=Favourite.objects.get(id=fid)
  item.delete()
  return redirect("/favviewpage")

def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']
      product_status=Products.objects.get(id=product_id)
      if product_status:
         if Favourite.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Favourite'}, status=200)
         else:
          Favourite.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Product Added to Favourite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)