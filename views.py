from django.shortcuts import render,redirect
from django.contrib import messages
from eapp .forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
from.models import category,Product


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/register')
   

def home_page(request):
    return render(request,'eapp/home.html')

def register_page(request): 
    form=CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration success you can login now")
            return redirect('/login')   
    return render(request,'eapp/register.html',{'form': form})

def collections(request):
    catagory= category.objects.all()
    return render(request,'eapp/collection.html',{"catagory":catagory})

def login_page(request):
    if request.method=="POST":
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"logged in successfully")
            return redirect('home')
        else:
            messages.error(request,"Invalid User Name or Password")
            return redirect ('login')
    return render(request,"eapp/login.html")
    
def collectionsview(request, cat_slug):
    if category.objects.filter(cat_slug=cat_slug):
        products = Product.objects.filter(categories__cat_slug=cat_slug)
        return render(request, 'eapp/product.html', {"products": products, "cat_slug": cat_slug})
    else:
        messages.warning(request, "No Such Category Found")
        return redirect('collections')
